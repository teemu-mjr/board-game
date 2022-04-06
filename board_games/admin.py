from django.contrib import admin

from .models import BoardGame, GameLoan

# Register your models here.


@admin.register(BoardGame)
class BoardGameAdmin(admin.ModelAdmin):
    list_display = ('Game', 'Genre', 'Year_published')

@admin.register(GameLoan)
class GameLoanAdmin(admin.ModelAdmin):
    list_display = ('Game', 'Loaner', 'Date_loaned')