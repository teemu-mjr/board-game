# Generated by Django 4.0.3 on 2022-04-06 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board_games', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boardgame',
            old_name='Year',
            new_name='Year_published',
        ),
    ]