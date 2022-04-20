from django import forms

from .models import BoardGame, GameLoan


class GameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ['game', 'genre', 'year_published']
        labels = {'game': 'Game', 'genre': 'Genre', 'description': 'Description',
                  'year_published': 'Year Published'}


class GameLoanForm(forms.ModelForm):
    class Meta:
        model = GameLoan
        fields = ['return_date']
        labels = {'return_date': 'Return date'}
