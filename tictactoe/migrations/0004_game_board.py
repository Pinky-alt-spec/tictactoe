# Generated by Django 3.1.7 on 2021-03-22 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0003_remove_game_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='board',
            field=models.CharField(default='         ', max_length=9),
        ),
    ]
