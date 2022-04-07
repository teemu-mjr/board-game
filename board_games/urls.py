from django.urls import path
from . import views

app_name = "board_games"
urlpatters = [
    # homepage
    path("", views.index, name="index"),
    # board games available
    path("games/", views.games, name="games"),
    # board game information
    path("games/<int:game_id>/", views.game_info, name="game_info"),
    # adding a new game
    path("new_game/", views.new_game, name="new_game"),
    # editing a game
    path("edit_game/<int:game_id>/", views.edit_game, name="edit_game"),
    # loaning a game
    path("new_loan/<int:game_id>/", views.new_loan, name="new_loan"),
    # edit loan
    path("edit_loan/<int:game_id>/", views.edit_loan, name="edit_loan"),
    # return game
    path("return_game/<int:game_id>/", views.return_game, name="return_game"),
]
