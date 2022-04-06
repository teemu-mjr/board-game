from socket import fromshare
from django import forms

from .models import BoardGame, GameLoan

class GameForm(forms.ModelForm):
    class Meta:
        model = BoardGame
        fields = ['Game', 'Genre', 'Year_published']
        labels = {'Year_published': 'Year Published'}

class GameLoan(forms.ModelForm):
    class Meta:
        model = GameLoan
        fields = ['Game', 'Loaner', 'Date_loaned']
        labels = {'Date_loaned': 'Date of loan'}