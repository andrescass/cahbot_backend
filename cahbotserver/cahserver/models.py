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


######################### FESTIVALES #################################

'''class FestMovie(models.Model):
    id = models.AutoField(primary_key = True)
    movie_name = models.CharField(max_length=300, blank=False, default='movie name')
    movie_director = models.CharField(max_length=150, blank=False, default='movie director')
    movie_country = models.CharField(max_length=150, blank=False, default='movie country')
    movie_year = models.IntegerField(blank=False, default=2021)
    movie_duration = models.IntegerField(blank=False, default=0)
    competition = models.CharField(max_length=150, blank=False, default=' ')
    date = models.CharField(max_length=150, blank=True, default='')
    sala = models.CharField(max_length=150, blank=True, default='')
    isOnline = models.CharField(max_length=150, blank=False, default='No')
    isCalos = models.CharField(max_length=150, blank=False, default='No')'''

class FestMovie(models.Model):
    id = models.AutoField(primary_key = True)
    movie_name = models.CharField(max_length=300, blank=False, default='movie name')
    movie_director = models.CharField(max_length=150, blank=False, default='movie director')
    movie_country = models.CharField(max_length=150, blank=False, default='movie country')
    competition = models.CharField(max_length=150, blank=False, default=' ')
    date = models.CharField(max_length=150, blank=True, default='')
    sala = models.CharField(max_length=150, blank=True, default='')
    isOnline = models.CharField(max_length=150, blank=False, default='No')
    isCalos = models.CharField(max_length=150, blank=False, default='No')

class WListEntry(models.Model):
    id = models.AutoField(primary_key = True)
    movie_id = models.IntegerField(blank=False, default=1)
    user_id = models.IntegerField(blank=False, default=1)
    seen = models.CharField(max_length=150, blank=True, default='No')

######################### OSCALOS #################################

class OscarEntry(models.Model):
    id = models.AutoField(primary_key = True)
    email = models.CharField(max_length=300, unique=True, blank=False)
    name = models.CharField(max_length=300, blank=False)
    selectedOptions = models.CharField(max_length=2000, blank=False)

####################### MIRALAS ANTES DE MORIR ######################

class MmamEntry(models.Model):
    id = models.AutoField(primary_key = True)
    email = models.CharField(max_length=300, unique=True, blank=False)
    name = models.CharField(max_length=300, blank=False)
    selectedOptions = models.CharField(max_length=2000, blank=False)

class MamColaborator(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=300, blank=True)
    mail = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f'{self.name}'

class MamMovie(models.Model):
    imdb_id = models.CharField(max_length=30, primary_key=True, unique=True, blank=False)
    rank = models.IntegerField(blank=False, default=1)
    points = models.IntegerField(blank=False, default=1)
    mentions_first = models.ManyToManyField(MamColaborator, blank=True, related_name='movie_first')
    mentions_other = models.ManyToManyField(MamColaborator, blank=True, related_name='movie_other')

class MamComment(models.Model):
    id = models.AutoField(primary_key = True)
    text = models.CharField(max_length=10000, blank=True)
    autor = models.ForeignKey(MamColaborator, related_name='comment', on_delete=models.CASCADE)
    movie = models.ForeignKey(MamMovie, related_name='review', on_delete=models.CASCADE)
    movie_imdb = models.CharField(max_length=20, blank=True)
    first_or_other = models.CharField(max_length=10, blank=True)