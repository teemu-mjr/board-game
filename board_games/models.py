from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BoardGame(models.Model):
    game = models.CharField(max_length=100)
    genre = models.CharField(max_length=200)
    year_published = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.game


class GameLoan(models.Model):
    game = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    date_loaned = models.DateTimeField()
    date_returned = models.DateTimeField()
