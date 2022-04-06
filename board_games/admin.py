from django.contrib import admin

from .models import BoardGame, GameLoan

# Register your models here.

admin.site.register(BoardGame)
admin.site.register(GameLoan)

#@admin.site.register(BoardGame)
#class GameAdmin(admin.ModelAdmin):
#    list_display = ('Game', 'Genre', 'Year_published')

#@admin.site.register(GameLoan)
#class LoanAdmin(admin.ModelAdmin):
#    list_display = ('Game', 'Loaner', 'Date_loaned')