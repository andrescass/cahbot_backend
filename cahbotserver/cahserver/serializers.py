from rest_framework import serializers
from cahserver.models import BlackCard, WhiteCard, GameGroup, Player, ScoreEntry, FestMovie, WListEntry, OscarEntry, MmamEntry

class BlackCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlackCard
        fields = ('id',
        'blancks',
        'phrase',
        'blanck_idx')

class WhiteCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhiteCard
        fields = ('id',
            'phrase',)

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('player_id',
        'name',
        'total_matchs',
        'total_points',
        'total_wons',)

class GameGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameGroup
        fields = ('group_id',
        'total_matchs',)

class ScoreEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreEntry
        fields = ('id',
        'player_id',
        'player_name',
        'group_id',
        'score',
        'matchs_won',
        'matchs_played',)
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }

######################### FESTIVALES #################################

class FestMovieSerializer(serializers.ModelSerializer):
    class Meta: 
        model = FestMovie
        fields = ('id',
        'movie_name',
        'movie_director',
        'movie_country',
        'movie_year',
        'movie_duration',
        'competition',
        'date',
        'sala',
        'isOnline',
        'isCalos')

class WListEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = WListEntry
        fields = ('id',
        'movie_id',
        'user_id',
        'seen')

class OscarEntrySereializer(serializers.ModelSerializer):
    class Meta:
        model = OscarEntry
        fields = '__all__'

class MmamEntrySereializer(serializers.ModelSerializer):
    class Meta:
        model = MmamEntry
        fields = '__all__'

