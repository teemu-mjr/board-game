# Generated by Django 4.0.3 on 2022-04-12 12:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('board_games', '0003_rename_game_boardgame_game_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameloan',
            name='date_returned',
        ),
        migrations.AddField(
            model_name='gameloan',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 12, 12, 54, 26, 448791, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gameloan',
            name='returned',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gameloan',
            name='date_loaned',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]