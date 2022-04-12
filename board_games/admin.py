from django.contrib import admin

from .models import BoardGame, GameLoan

# Register your models here.


@admin.register(BoardGame)
class BoardGameAdmin(admin.ModelAdmin):
    list_display = ('game', 'genre', 'year_published', "loaned")


@admin.register(GameLoan)
class GameLoanAdmin(admin.ModelAdmin):
    list_display = ('game', 'date_loaned')
