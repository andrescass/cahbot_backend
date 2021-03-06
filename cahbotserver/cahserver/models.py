from django.db import models

# Create your models here.
class BlackCard(models.Model):
    id = models.AutoField(primary_key=True)
    blancks = models.IntegerField(blank=True, default=1)
    phrase = models.CharField(max_length=300, blank=False, default='')
    blanck_idx = models.IntegerField(blank=True, default=1)

    def __str__(self):
        return self.phrase

class WhiteCard(models.Model):
    id = models.AutoField(primary_key=True)
    phrase = models.CharField(max_length=150, blank=False, default='')

    def __str__(self):
        return self.phrase

class Player(models.Model):
    player_id = models.IntegerField(primary_key=True, unique=True, blank=False, default=1)
    name = models.CharField(max_length=150, blank=False, default='')
    total_matchs = models.IntegerField(blank=False, default=1)
    total_points = models.IntegerField(blank=False, default=0)
    total_wons = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return self.name

class GameGroup(models.Model):
    group_id = models.IntegerField(primary_key=True, unique=True, blank=False, default=1)
    total_matchs = models.IntegerField(blank=False, default=1)

    def __str__(self):
        return "{0}".format(self.group_id)

class ScoreEntry(models.Model):
    id = models.AutoField(primary_key = True)
    player_id = models.IntegerField(blank=False, default=1)
    player_name = models.CharField(max_length=150, blank=False, default='')
    group_id = models.IntegerField(blank=False, default=1)
    score = models.IntegerField(blank=False, default=0)
    matchs_won = models.IntegerField(blank=False, default=0)
    matchs_played = models.IntegerField(blank=False, default=1)

    def __str__(self):
        return "{0} : {1}".format(self.group_id, self.player_id)


