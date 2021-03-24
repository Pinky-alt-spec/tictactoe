# Generated by Django 3.1.7 on 2021-03-22 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tictactoe', '0004_game_board'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='board',
        ),
        migrations.AddField(
            model_name='game',
            name='game_opponent',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]