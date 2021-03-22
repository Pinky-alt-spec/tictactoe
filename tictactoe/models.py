from django.db import models


# Create your models here.


class Game(models.Model):
    room_code = models.CharField(max_length=100)
    game_creator = models.CharField(max_length=100)
    game_opponent = models.CharField(max_length=100, blank=True, null=True)
    is_over = models.BooleanField(default=False)
    # board = models.CharField(max_length=9, default=" " * 9)
    # player_1 = models.CharField(max_length=64)
    # player_2 = models.CharField(max_length=64)
    # cell = models.CharField(max_length=1)

    def __str__(self):
        return self.game_creator
