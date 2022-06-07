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
    url('api/fest_movies_del/delete_movies/', csrf_exempt(views.delete_movies)),
    url(r'^api/oscalo/check$', csrf_exempt(views.check_oscalo)),
    url(r'^api/oscalo/newoscalo$', csrf_exempt(views.create_oscalo)),
    path('api/oscalo/delete_oscalo/<pk>', csrf_exempt(views.delete_oscalo)),
    url(r'^api/mam/check$', csrf_exempt(views.check_mam)),
    url(r'^api/mam/newmam$', csrf_exempt(views.create_mam)),
    path('api/mam/delete_mam/<pk>', csrf_exempt(views.delete_mam)),
    url(r'^api/mam/get_colabs$', csrf_exempt(views.get_colabs)),
    url(r'^api/mam/newcolab$', csrf_exempt(views.create_colab)),
    path('api/mam/delete_colab/<pk>', csrf_exempt(views.delete_colab)),
    url(r'^api/mam/get_movies$', csrf_exempt(views.get_movies)),
    url(r'^api/mam/newmovie$', csrf_exempt(views.create_movie)),
    path('api/mam/delete_movie/<pk>', csrf_exempt(views.delete_movie)),
    url(r'^api/mam/get_revs$', csrf_exempt(views.get_revs)),
    url(r'^api/mam/newrev$', csrf_exempt(views.create_rev)),
    path('api/mam/delete_rev/<pk>', csrf_exempt(views.delete_rev)),
]