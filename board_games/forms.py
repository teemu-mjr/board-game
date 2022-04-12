from django import forms

from .models import BoardGame, GameLoan


class GameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ['game', 'genre', 'year_published']
        labels = {'game': 'Game', 'genre': 'Genre',
                  'year_published': 'Year Published'}


class GameLoanForm(forms.ModelForm):
    class Meta:
        model = GameLoan
        fields = ['game', 'return_date']
        labels = {'game': 'Game', 'return_date': 'Return date'}




