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
        fields = ['game', 'date_loaned', 'date_returned']
        labels = {'date_loaned': 'Date of loan',
                  'date_returned': 'Date Returned'}
