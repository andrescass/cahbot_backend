from rest_framework import serializers
from cahserver.models import BlackCard, WhiteCard, GameGroup, Player, ScoreEntry

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
