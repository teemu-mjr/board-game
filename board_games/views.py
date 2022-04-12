from django.http import Http404
from django.shortcuts import redirect, render

from .forms import GameForm, GameLoanForm
from .models import BoardGame, GameLoan

# Create your views here.


def index(request):
    """The index page"""
    return render(request, "board_games/index.html")


def games(request):
    """Shows all the games available"""
    games = BoardGame.objects.order_by("game")
    context = {"games": games}
    return render(request, "board_games/games.html", context)


def game_info(request, game_id):
    """Shows information about given game"""
    game = BoardGame.objects.get(id=game_id)
    # TODO add game loan history
    context = {"game": game}
    return render(request, "board_games/game_info.html", context)


def add_game(request):
    """Adds a new game to the database"""
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


def edit_game(request, game_id):
    """Adds a new game to the database"""
    game = BoardGame.objects.get(id=game_id)

    # if loan.owner != request.user:
    #     raise Http404

    if request.method != "POST":
        form = GameForm(instance=game)

    else:
        form = GameForm(instance=game, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect("board_games:game_info", game_id)

    context = {"game": game, "form": form}
    return render(request, "board_games/edit_game.html", context)


def add_loan(request, game_id):
    """Adds a new game to the database"""
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
            # TODO redirect to the user loans?
            return redirect("board_games:games")

    context = {"game": game, "form": form}
    return render(request, "board_games/add_loan.html", context)


def edit_loan(request, loan_id):
    """Adds a new game to the database"""
    loan = GameLoan.objects.get(id=loan_id)
    game = loan.game

    # if loan.owner != request.user:
    #     raise Http404

    if request.method != "POST":
        form = GameLoanForm(instance=loan)

    else:
        form = GameLoanForm(instance=loan, data=request.POST)

        if form.is_valid():
            form.save()
            # TODO redirect to game loans
            return redirect("board_games:games")

    context = {"loan": loan, "game": game, "form": form}
    return render(request, "board_games/edit_loan.html", context)


def return_game(request):
    """TODO Adds a new game to the database"""
    return render(request, "board_games/return_game.html")
