from django.db import models

# Create your models here.

class GameType(models.Model):
    name = models.CharField(primary_key=True, max_length=255)


class Bet(models.Model):
    player1 = models.CharField(max_length=255)
    player2 = models.CharField(max_length=255)
    spread = models.FloatField(default=0)
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)




