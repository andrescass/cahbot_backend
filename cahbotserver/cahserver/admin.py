from django.contrib import admin
from .models import BlackCard, WhiteCard, GameGroup, Player, ScoreEntry

# Register your models here.
admin.site.register(BlackCard)
admin.site.register(WhiteCard)
admin.site.register(GameGroup)
admin.site.register(Player)
admin.site.register(ScoreEntry)
