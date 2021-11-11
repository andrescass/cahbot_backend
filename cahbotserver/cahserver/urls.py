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
    path('api/delete_cards/<keyword>', csrf_exempt(views.delete_cards)),
    url('api/fest_movies/', csrf_exempt(views.movie_list)),
    url('api/watch_lists/', csrf_exempt(views.wlist_list)),
    path('api/user_wlist/<pk>', csrf_exempt(views.user_wlist)),
    path('api/user_wlist/delete/<pk>', csrf_exempt(views.delete_cite)),
    path('api/fest_movie/delete/<pk>', csrf_exempt(views.delete_movie)),
    path('api/user_wlist_seen/<pk>', csrf_exempt(views.set_seen)),
    url('api/fest_movies/delete_movies/', csrf_exempt(views.delete_movies)),
]