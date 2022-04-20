from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BoardGame(models.Model):
    game = models.CharField(max_length=100)
    genre = models.CharField(max_length=200)
    year_published = models.IntegerField()
    description = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    loaned = models.BooleanField(default=False)

    def __str__(self):
        return self.game


class GameLoan(models.Model):
    game = models.ForeignKey(BoardGame, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_loaned = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField()
    returned = models.BooleanField(default=False)
