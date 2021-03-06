from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render

from .forms import GameForm, GameLoanForm
from .models import BoardGame, GameLoan

# Create your views here.


def index(request):
    """The index page"""
    return render(request, "board_games/index.html")


@login_required
def games(request):
    """Shows all the games available"""
    games = BoardGame.objects.order_by("game")
    context = {"games": games}
    return render(request, "board_games/games.html", context)


@login_required
def loans(request):
    """Shows all users loans"""
    loans = GameLoan.objects.filter(returned=False).filter(owner=request.user)
    context = {"loans": loans}
    return render(request, "board_games/loans.html", context)


@login_required
def game_info(request, game_id):
    """Shows information about given game"""
    game = BoardGame.objects.get(id=game_id)
    loans = GameLoan.objects.filter(game=game).order_by("-id")
    context = {"game": game, "loans": loans}
    return render(request, "board_games/game_info.html", context)


@login_required
def add_game(request):
    """Adds a new game"""
    if request.method != "POST":
        form = GameForm()

    else:
        form = GameForm(request.POST)
        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.owner = request.user
            new_game.save()
            return redirect("board_games:games")

    context = {"form": form}
    return render(request, "board_games/add_game.html", context)


@login_required
def edit_game(request, game_id):
    """Edit a game"""
    game = BoardGame.objects.get(id=game_id)

    if game.owner != request.user:
        raise Http404

    if request.method != "POST":
        form = GameForm(instance=game)

    else:
        form = GameForm(instance=game, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect("board_games:game_info", game_id)

    context = {"game": game, "form": form}
    return render(request, "board_games/edit_game.html", context)


@login_required
def add_loan(request, game_id):
    """Adds a new loan"""
    game = BoardGame.objects.get(id=game_id)

    if request.method != "POST":
        form = GameLoanForm()

    else:
        form = GameLoanForm(request.POST)
        if form.is_valid():
            new_loan = form.save(commit=False)
            new_loan.game = game
            new_loan.owner = request.user
            new_loan.save()
            game.loaned = True
            game.save()
            return redirect("board_games:loans")

    context = {"game": game, "form": form}
    return render(request, "board_games/add_loan.html", context)


@login_required
def edit_loan(request, loan_id):
    """Editing a loan"""
    loan = GameLoan.objects.get(id=loan_id)

    if loan.owner != request.user:
        raise Http404

    if request.method != "POST":
        form = GameLoanForm(instance=loan)

    else:
        form = GameLoanForm(instance=loan, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect("board_games:loans")

    context = {"loan": loan, "form": form}
    return render(request, "board_games/edit_loan.html", context)


@login_required
def return_game(request, loan_id):
    """Returns the game given"""
    loan = GameLoan.objects.get(id=loan_id)
    loan.returned = True
    loan.game.loaned = False
    loan.game.save()
    loan.save()
    return redirect("board_games:loans")
