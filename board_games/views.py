from django.shortcuts import render

# Create your views here.


def index(request):
    """The index page"""
    return render(request, "board_games/index.html")


def games(request):
    """Shows all the games available"""
    return render(request, "board_games/games.html")


def game_info(request):
    """Shows information about given game"""
    return render(request, "board_games/game_info.html")


def new_game(request):
    """Adds a new game to the database"""
    return render(request, "board_games/new_game.html")


def edit_game(request):
    """Adds a new game to the database"""
    return render(request, "board_games/edit_game.html")


def new_loan(request):
    """Adds a new game to the database"""
    return render(request, "board_games/new_loan.html")


def edit_loan(request):
    """Adds a new game to the database"""
    return render(request, "board_games/edit_loan.html")


def return_game(request):
    """Adds a new game to the database"""
    return render(request, "board_games/return_game.html")
