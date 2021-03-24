from django.db import models


# Create your models here.


class Game(models.Model):
    room_code = models.CharField(max_length=100)
    game_creator = models.CharField(max_length=100)
    game_opponent = models.CharField(max_length=100, blank=True, null=True)
    is_over = models.BooleanField(default=True)

    # def __str__(self):
    #     return self.game_creator

    class Meta:
        db_table = "tictactoe_game"

