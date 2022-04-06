from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BoardGame(models.Model):
    Game = models.CharField(max_length=100)
    Genre = models.CharField(max_length=200)
    Year_published = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Game


class GameLoan(models.Model):
    Game = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    Loaner = models.CharField(max_length=200)
    Date_loaned = models.DateTimeField(auto_now=True)



