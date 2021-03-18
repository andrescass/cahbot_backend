from django.conf.urls import url 
from cahserver import views 
from django.views.decorators.csrf import csrf_exempt
from django.urls import path, include

urlpatterns = [
    url('api/bc/', csrf_exempt(views.black_card_list)),
    url('api/wc/', csrf_exempt(views.white_card_list)),
    path('api/randombc/<n>', csrf_exempt(views.black_card_random_list)),
    path('api/randomwc/<n>', csrf_exempt(views.white_card_random_list)),
    url('api/gamegroups/', csrf_exempt(views.group_list)),
    url('api/players/', csrf_exempt(views.player_list)),
    url('api/score_entries/', csrf_exempt(views.score_entries)),
    path('api/group_table/<pk>', csrf_exempt(views.group_table)),
    path('api/player_table/<pk>', csrf_exempt(views.player_table)),
]