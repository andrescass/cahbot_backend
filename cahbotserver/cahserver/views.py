from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from random import sample

from cahserver.models import BlackCard, WhiteCard, GameGroup, Player, ScoreEntry, FestMovie, WListEntry, OscarEntry, MmamEntry, MamColaborator, MamComment, MamMovie
from cahserver.serializers import BlackCardSerializer, WhiteCardSerializer, GameGroupSerializer, PlayerSerializer, ScoreEntrySerializer, FestMovieSerializer, WListEntrySerializer, OscarEntrySereializer, MmamEntrySereializer
from cahserver.serializers import MmaColabSereializer, MamMovieSerializer, MamCommentSerializer

# Create your views here.


# Cards
@api_view(['GET', 'POST'])
def black_card_list(request):
    if request.method == 'GET':
        try:
            bcList = BlackCard.objects.all()
            bc_serializer = BlackCardSerializer(bcList, many=True)
            response = {
                'message': "Get all black cards succefully",
                'black_cards': bc_serializer.data,
                'error': ''
            }
            return JsonResponse(bc_serializer.data, safe=False)
        except:
            error = {
                'message': "Fail! -> can NOT get all the cards. Please check again!",
                'blac_cards': "[]",
                'error': "Error"
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'POST':
        try:
            
            bcData = JSONParser().parse(request)
            bc_serialized = BlackCardSerializer(data=bcData)
            if bc_serialized.is_valid():
                bc_serialized.save()
                return JsonResponse(bc_serialized.data, status=status.HTTP_201_CREATED)
            else:
                error = {
                    'message':"Can Not upload successfully!",
                    'cards':"[]",
                    'error': bc_serializer.errors
                    }
                return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(ex)
            exceptionError = {
                'message': "Can Not upload successfully!",
                'cards': "[]",
                'error': "Having an exception!"
                }
            return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def black_card_random_list(request, n):
    if request.method == 'GET':
        try:
            bcList = BlackCard.objects.all()
            if int(n) >= len(list(bcList)):
                n = len(list(bcList))
            random_bcList = sample(list(bcList), int(n))
            bc_serializer = BlackCardSerializer(random_bcList, many=True)
            response = {
                'message': "Get all black cards succefully",
                'black_cards': bc_serializer.data,
                'error': ''
            }
            return JsonResponse(bc_serializer.data, safe=False)
        except Exception as ex:
            print(ex)
            error = {
                'message': "Fail! -> can NOT get all the cards. Please check again!",
                'blac_cards': "[]",
                'error': "Error"
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(['GET', 'POST'])
def white_card_list(request):
    if request.method == 'GET':
        try:
            wcList = WhiteCard.objects.all()
            wc_serializer = WhiteCardSerializer(wcList, many=True)
            response = {
                'message': "Get all black cards succefully",
                'white_cards': wc_serializer.data,
                'error': ''
            }
            return JsonResponse(wc_serializer.data, safe=False)
        except Exception as ex:
            print(ex)
            error = {
                'message': "Fail! -> can NOT get all the cards. Please check again!",
                'white_cards': "[]",
                'error': "Error"
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'POST':
        try:
            
            wcData = JSONParser().parse(request)
            wc_serialized = WhiteCardSerializer(data=wcData)
            if wc_serialized.is_valid():
                wc_serialized.save()
                return JsonResponse(wc_serialized.data, status=status.HTTP_201_CREATED)
            else:
                error = {
                    'message':"Can Not upload successfully!",
                    'cards':"[]",
                    'error': wc_serializer.errors
                    }
                return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(ex)
            exceptionError = {
                'message': "Can Not upload successfully!",
                'cards': "[]",
                'error': "Having an exception!"
                }
            return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def white_card_random_list(request, n):
    if request.method == 'GET':
        try:
            wcList = WhiteCard.objects.all()
            if int(n) >= len(list(wcList)):
                n = len(list(wcList))
            random_wcList = sample(list(wcList), int(n))
            wc_serializer = WhiteCardSerializer(random_wcList, many=True)
            response = {
                'message': "Get all black cards succefully",
                'white_cards': wc_serializer.data,
                'error': ''
            }
            return JsonResponse(wc_serializer.data, safe=False)
        except Exception as ex:
            print(ex)
            error = {
                'message': "Fail! -> can NOT get all the cards. Please check again!",
                'white_cards': "[]",
                'error': "Error"
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_cards(request, keyword):
    if request.method == 'DELETE':
        try:
            if keyword == "whitecards":
                count = WhiteCard.objects.all().delete()
                return JsonResponse({'message': '{} white cards were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
            elif keyword == "blackcards":
                count = BlackCard.objects.all().delete()
                return JsonResponse({'message': '{} black cards were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
            else:
                return JsonResponse({'message': 'Bad keyword'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            print(ex)
            error = {
                'message': "Fail! -> can NOT delete the cards. Please check again!",
                'white_cards': "[]",
                'error': "Error"
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

##### Game Groups ######

@api_view(['GET', 'POST'])
def group_list(request):
    if request.method == 'GET':
        try:
            groupList = GameGroup.objects.all()
            group_serializer = GameGroupSerializer(groupList, many=True)
            response = {
                'message': "Get all black cards succefully",
                'game_groups': group_serializer.data,
                'error': ''
            }
            return JsonResponse(group_serializer.data, safe=False)
        except Exception as ex:
            print(ex)
            error = {
                'message': "Fail! -> can NOT get all the groups. Please check again!",
                'game_groups': "[]",
                'error': "Error"
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'POST':
        try:
            groupData = JSONParser().parse(request)
            group_serialized = GameGroupSerializer(data=groupData)
            if group_serialized.is_valid():
                group_serialized.save()
                return JsonResponse(group_serialized.data, status=status.HTTP_201_CREATED)
            else:
                error = {
                    'message':"Can Not upload successfully!",
                    'cards':"[]",
                    'error': group_serialized.errors
                    }
                return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(ex)
            exceptionError = {
                'message': "Can Not upload successfully!",
                'cards': "[]",
                'error': "Having an exception!"
                }
            return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

##### Players #####

@api_view(['GET', 'POST'])
def player_list(request):
    if request.method == 'GET':
        try:
            playerList = Player.objects.all()
            player_serializer = PlayerSerializer(playerList, many=True)
            response = {
                'message': "Get all black cards succefully",
                'game_groups': player_serializer.data,
                'error': ''
            }
            return JsonResponse(player_serializer.data, safe=False)
        except Exception as ex:
            print(ex)
            error = {
                'message': "Fail! -> can NOT get all the players. Please check again!",
                'players': "[]",
                'error': "Error"
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'POST':
        try:
            playerData = JSONParser().parse(request)
            player_serialized = PlayerSerializer(data=playerData)
            if player_serialized.is_valid():
                player_serialized.save()
                return JsonResponse(player_serialized.data, status=status.HTTP_201_CREATED)
            else:
                error = {
                    'message':"Can Not upload successfully!",
                    'cards':"[]",
                    'error': player_serialized.errors
                    }
                return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(ex)
            exceptionError = {
                'message': "Can Not upload successfully!",
                'cards': "[]",
                'error': "Having an exception!"
                }
            return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Score Entries
@api_view(['GET', 'POST'])
def score_entries(request):
    if request.method == 'GET':
        try:
            scoreList = ScoreEntry.objects.all()
            score_serializer = ScoreEntrySerializer(scoreList, many=True)
            response = {
                'message': "Get all scroe entries succefully",
                'game_groups': score_serializer.data,
                'error': ''
            }
            return JsonResponse(score_serializer.data, safe=False)
        except Exception as ex:
            print(ex)
            error = {
                'message': "Fail! -> can NOT get all the scores. Please check again!",
                'players': "[]",
                'error': "Error"
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'POST':
        try:
            scoreData = JSONParser().parse(request)
            score_serialized = ScoreEntrySerializer(data=scoreData)
            if score_serialized.is_valid():
                if Player.objects.filter(player_id=score_serialized.validated_data['player_id']).exists():
                    player = Player.objects.get(player_id=score_serialized.validated_data['player_id'])
                    player.total_matchs += 1
                    player.total_points += score_serialized.validated_data['score']
                    player.total_wons += score_serialized.validated_data['matchs_won']
                    player.save()
                else:
                    player = Player(player_id = score_serialized.validated_data['player_id'])
                    player.name = score_serialized.validated_data['player_name']
                    player.total_matchs = 1
                    player.total_points = score_serialized.validated_data['score']
                    player.total_wons = score_serialized.validated_data['matchs_won']
                    player.save()

                if GameGroup.objects.filter(group_id=score_serialized.validated_data['group_id']).exists():
                    gr = GameGroup.objects.get(group_id=score_serialized.validated_data['group_id'])
                    gr.total_matchs += 1
                    gr.save()
                else:
                    gr = GameGroup(group_id=score_serialized.validated_data['group_id'], total_matchs=1)
                    gr.save()

                if ScoreEntry.objects.filter(group_id=score_serialized.validated_data['group_id']).exists():
                    score_list = ScoreEntry.objects.filter(group_id=score_serialized.validated_data['group_id'])
                    founded = False
                    for sc in score_list:
                        if sc.player_id == score_serialized.validated_data['player_id']:
                            founded = True
                            sc.matchs_played += 1
                            sc.matchs_won += score_serialized.validated_data['matchs_won']
                            sc.score += score_serialized.validated_data['score']
                            sc.save()
                            break
                    if founded == False:
                        score_serialized.save()
                else:
                    score_serialized.save()
                return JsonResponse(score_serialized.data, status=status.HTTP_201_CREATED)
            else:
                error = {
                    'message':"Can NOT upload successfully!",
                    'cards':"[]",
                    'error': score_serialized.errors
                    }
                return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(ex)
            exceptionError = {
                'message': "Can Not upload successfully!",
                'cards': "[]",
                'error': "Having an exception!"
                }
            return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def group_table(request, pk):
    try:
        if ScoreEntry.objects.filter(group_id=pk).exists():
            score_list = ScoreEntry.objects.filter(group_id=pk)
            score_serializer = ScoreEntrySerializer(score_list, many=True)
            response = {
                'message': "Get all score entries succefully",
                'game_groups': score_serializer.data,
                'error': ''
            }
            return JsonResponse(score_serializer.data, safe=False)
        else:
            response = {
                'message': "No score entries for this group",
                'error': 'No entries yet'
            }
            return JsonResponse(response, safe=False)
    except Exception as ex:
        print(ex)
        exceptionError = {
            'message': "Can Not get entries!",
            'cards': "[]",
            'error': "Having an exception!"
            }
        return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def player_table(request, pk):
    try:
        if Player.objects.filter(player_id=pk).exists():
            player = Player.objects.get(player_id=pk)
            player_serializer = PlayerSerializer(player)
            response = {
                'message': "Get all score entries succefully",
                'game_groups': player_serializer.data,
                'error': ''
            }
            return JsonResponse(player_serializer.data, safe=False)
        else:
            response = {
                'message': "No score entries for this player",
                'error': 'No entries yet'
            }
            return JsonResponse(response, safe=False)
    except Exception as ex:
        print(ex)
        exceptionError = {
            'message': "Can Not get entries!",
            'cards': "[]",
            'error': "Having an exception!"
            }
        return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

######################### FESTIVALES #################################
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        try:
            movieList = FestMovie.objects.all()
            movie_serializer = FestMovieSerializer(movieList, many=True)
            response = {
                'message': "Get all movies succefully",
                'movies': movie_serializer.data,
                'error': ''
            }
            return JsonResponse(movie_serializer.data, safe=False)
        except Exception as ex:
            print(ex)
            error = {
                'message': "Fail! -> can NOT get all the movies. Please check again!",
                'movies': "[]",
                'error': "Error"
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'POST':
        try:
            
            movieData = JSONParser().parse(request)
            movie_serializer = FestMovieSerializer(data=movieData)
            if movie_serializer.is_valid():
                movie_serializer.save()
                return JsonResponse(movie_serializer.data, status=status.HTTP_201_CREATED)
            else:
                error = {
                    'message':"Can Not upload successfully!",
                    'movies':"[]",
                    'error': movie_serializer.errors
                    }
                return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(ex)
            exceptionError = {
                'message': "Can Not upload successfully!",
                'movies': "[]",
                'error': "Having an exception!"
                }
            return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'POST'])
def wlist_list(request):
    if request.method == 'GET':
        try:
            wlistList = WListEntry.objects.all()
            wlist_serializer = WListEntrySerializer(wlistList, many=True)
            response = {
                'message': "Get all wlists succefully",
                'wlists': wlist_serializer.data,
                'error': ''
            }
            return JsonResponse(wlist_serializer.data, safe=False)
        except Exception as ex:
            print(ex)
            error = {
                'message': "Fail! -> can NOT get all the wlists. Please check again!",
                'wlits': "[]",
                'error': "Error"
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'POST':
        try:
            
            wlistData = JSONParser().parse(request)
            wlist_serialized = WListEntrySerializer(data=wlistData)
            if wlist_serialized.is_valid():
                wlist_serialized.save()
                return JsonResponse(wlist_serialized.data, status=status.HTTP_201_CREATED)
            else:
                error = {
                    'message':"Can Not upload successfully!",
                    'wlits':"[]",
                    'error': wlist_serializer.errors
                    }
                return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(ex)
            exceptionError = {
                'message': "Can Not upload successfully!",
                'wlists': "[]",
                'error': "Having an exception! " + repr(ex)
                }
            return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def user_wlist(request, pk):
    try:
        if WListEntry.objects.filter(user_id=pk).exists():
            wlist = WListEntry.objects.filter(user_id=pk)
            wlist_serializer = WListEntrySerializer(wlist, many=True)
            response = {
                'message': "Get all entries succefully",
                'wlist': wlist_serializer.data,
                'error': ''
            }
            return JsonResponse(wlist_serializer.data, safe=False)
        else:
            response = {
                'message': "No entries for this user",
                'error': 'No entries yet'
            }
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
    except Exception as ex:
        print(ex)
        exceptionError = {
            'message': "Can Not get entries!",
            'cards': "[]",
            'error': "Having an exception!" + repr(ex)
            }
        return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_cite(request, pk):
    if request.method == 'DELETE':
        try:
            if WListEntry.objects.filter(id=pk).exists():
                count = WListEntry.objects.get(id=pk).delete()
            return JsonResponse({'message': '{} white cards were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            print(ex)
            error = {
                'message': "Fail! -> can NOT delete the cards. Please check again!",
                'white_cards': "[]",
                'error': "Error"
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_movie(request, pk):
    if request.method == 'DELETE':
        try:
            if FestMovie.objects.filter(id=pk).exists():
                count = FestMovie.objects.get(id=pk).delete()
            return JsonResponse({'message': '{} white cards were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            print(ex)
            error = {
                'message': "Fail! -> can NOT delete the cards. Please check again!",
                'white_cards': "[]",
                'error': "Error" + + repr(ex)
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def set_seen(request, pk):
    if request.method == 'PUT':
        try:
            wl = WListEntry.objects.get(id=pk)
            wl.seen = 'Si'
            wl.save()
            return JsonResponse('Updated', safe=False)
        except Exception as ex:
            print(ex)
            error = {
                'message': "Fail!",
                'white_cards': "[]",
                'error': "Error" + repr(ex)
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_movies(request):
    if request.method == 'DELETE':
        try:
            count = FestMovie.objects.all().delete()
            return JsonResponse({'message': '{} movies were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            error = {
                'message': "Fail! -> can NOT delete the movies",
                'white_cards': "[]",
                'error': "Error" + repr(ex)
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


################### Oscalos ###################

@api_view(['GET', 'POST'])
def check_oscalo(request):
    if request.method == 'POST':
        try:
            data_oscar = JSONParser().parse(request)
            email_exists = OscarEntry.objects.filter(email=data_oscar['email']).exists()
            if email_exists:
                response = {
                    'message': "Get all wlists succefully",
                    'exists': True,
                    'error': ''
                }
            else:
                response = {
                    'message': "Get all wlists succefully",
                    'exists': False,
                    'error': ''
                }
            return JsonResponse(response, status=status.HTTP_201_CREATED)
        except Exception as ex:
            print(ex)
            error = {
                'message': "Fail! -> can NOT access to server. Please check again!",
                'error': "Error" + repr(ex)
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'GET':
        oscaloList = OscarEntry.objects.all()
        oscalo_serializer = OscarEntrySereializer(oscaloList, many=True)
        response = {
            'message': "Get all oscalos succefully",
            'wlists': oscalo_serializer.data,
            'error': ''
        }
        return JsonResponse(oscalo_serializer.data, safe=False)

@api_view(['POST'])
def create_oscalo(request):
    if request.method == 'POST':
        try: 
            oscalo = JSONParser().parse(request)
            oscalo_serialized = OscarEntrySereializer(data=oscalo)
            if oscalo_serialized.is_valid():
                oscalo_serialized.save()
                return JsonResponse(oscalo_serialized.data, status=status.HTTP_201_CREATED)
            else:
                error = {
                    'message':"Can Not upload successfully!",
                    'wlits':"[]",
                    'error': oscalo_serialized.errors
                    }
                return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(ex)
            exceptionError = {
                'message': "Can Not upload successfully!",
                'wlists': "[]",
                'error': "Having an exception! " + repr(ex)
                }
            return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_oscalo(request, pk):
    if request.method == 'DELETE':
        try:
            if OscarEntry.objects.filter(id=pk).exists():
                count = OscarEntry.objects.get(id=pk).delete()
            return JsonResponse({'message': '{} white cards were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            print(ex)
            error = {
                'message': "Fail! -> can NOT delete the cards. Please check again!",
                'white_cards': "[]",
                'error': "Error" + + repr(ex)
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

######################### MAMM #######################

@api_view(['GET', 'POST'])
def check_mam(request):
    if request.method == 'POST':
        try:
            data_mam = JSONParser().parse(request)
            email_exists = MmamEntry.objects.filter(email=data_mam['email']).exists()
            if email_exists:
                response = {
                    'message': "Email already registered",
                    'exists': True,
                    'error': ''
                }
            else:
                response = {
                    'message': "Email not registered",
                    'exists': False,
                    'error': ''
                }
            return JsonResponse(response, status=status.HTTP_201_CREATED)
        except Exception as ex:
            print(ex)
            error = {
                'message': "Fail! -> can NOT access to server. Please check again!",
                'error': "Error" + repr(ex)
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'GET':
        mamList = MmamEntry.objects.all()
        mam_serializer = MmamEntrySereializer(mamList, many=True)
        response = {
            'message': "Get all mam succefully",
            'wlists': mam_serializer.data,
            'error': ''
        }
        return JsonResponse(mam_serializer.data, safe=False)

@api_view(['POST'])
def create_mam(request):
    if request.method == 'POST':
        try: 
            mam = JSONParser().parse(request)
            mam_serialized = MmamEntrySereializer(data=mam)
            if mam_serialized.is_valid():
                mam_serialized.save()
                return JsonResponse(mam_serialized.data, status=status.HTTP_201_CREATED)
            else:
                error = {
                    'message':"Can Not upload successfully!",
                    'wlits':"[]",
                    'error': mam_serialized.errors
                    }
                return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(ex)
            exceptionError = {
                'message': "Can Not upload successfully!",
                'wlists': "[]",
                'error': "Having an exception! " + repr(ex)
                }
            return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_mam(request, pk):
    if request.method == 'DELETE':
        try:
            if MmamEntry.objects.filter(id=pk).exists():
                count = MmamEntry.objects.get(id=pk).delete()
            return JsonResponse({'message': '{} entries were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            print(ex)
            error = {
                'message': "Fail! -> can NOT delete the entry. Please check again!",
                'white_cards': "[]",
                'error': "Error" + + repr(ex)
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

##### Coaborators

@api_view(['GET'])
def get_colabs(request):
    if request.method == 'GET':
        mamList = MamColaborator.objects.all()
        mam_serializer = MmaColabSereializer(mamList, many=True)
        response = {
            'message': "Get all colaborators succefully",
            'wlists': mam_serializer.data,
            'error': ''
        }
        return JsonResponse(mam_serializer.data, safe=False)

@api_view(['POST'])
def create_colab(request):
    if request.method == 'POST':
        try: 
            mam = JSONParser().parse(request)
            mam_serialized = MmaColabSereializer(data=mam)
            if mam_serialized.is_valid():
                mam_serialized.save()
                return JsonResponse(mam_serialized.data, status=status.HTTP_201_CREATED)
            else:
                error = {
                    'message':"Can Not upload successfully!",
                    'wlits':"[]",
                    'error': mam_serialized.errors
                    }
                return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(ex)
            exceptionError = {
                'message': "Can Not upload successfully!",
                'wlists': "[]",
                'error': "Having an exception! " + repr(ex)
                }
            return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_colab(request, pk):
    if request.method == 'DELETE':
        try:
            if MamColaborator.objects.filter(id=pk).exists():
                count = MamColaborator.objects.get(id=pk).delete()
            return JsonResponse({'message': '{} colaborator were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            print(ex)
            error = {
                'message': "Fail! -> can NOT delete the entry. Please check again!",
                'white_cards': "[]",
                'error': "Error" + + repr(ex)
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

##### Movies

@api_view(['GET'])
def get_movies(request):
    if request.method == 'GET':
        movieList = MamMovie.objects.all().order_by('rank')
        movie_serializer = MamMovieSerializer(movieList, many=True)
        response = {
            'message': "Get all movies succefully",
            'wlists': movie_serializer.data,
            'error': ''
        }
        return JsonResponse(movie_serializer.data, safe=False)

@api_view(['POST'])
def create_movie(request):
    if request.method == 'POST':
        try: 
            movie = JSONParser().parse(request)
            movie_serialized = MamMovieSerializer(data=movie)
            if movie_serialized.is_valid():
                mm = MamMovie(imdb_id = movie_serialized.validated_data['imdb_id'],
                rank =movie_serialized.validated_data['rank'],
                points = movie_serialized.validated_data['points'])
                mm.save()
                for colab_f in movie_serialized.validated_data['mentions_first']:
                    if MamColaborator.objects.filter(mail=colab_f['mail']).exists():
                        m_colab_f = MamColaborator.objects.get(mail=colab_f['mail'])
                        mm.mentions_first.add(m_colab_f)
                for colab_o in movie_serialized.validated_data['mentions_other']:
                    if MamColaborator.objects.filter(mail=colab_o['mail']).exists():
                        m_colab_o = MamColaborator.objects.get(mail=colab_o['mail'])
                        mm.mentions_other.add(m_colab_o)
                mm.save()
                ms = MamMovieSerializer(mm)
                return JsonResponse(ms.data, status=status.HTTP_201_CREATED)
            else:
                error = {
                    'message':"Can Not upload successfully!",
                    'wlits':"[]",
                    'error': movie_serialized.errors
                    }
                return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(ex)
            exceptionError = {
                'message': "Can Not upload successfully!",
                'wlists': "[]",
                'error': "Having an exception! " + repr(ex)
                }
            return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_movie(request, pk):
    if request.method == 'DELETE':
        try:
            if MamMovie.objects.filter(imdb_id=pk).exists():
                count = MamMovie.objects.get(imdb_id=pk).delete()
            return JsonResponse({'message': '{} movie were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            print(ex)
            error = {
                'message': "Fail! -> can NOT delete the entry. Please check again!",
                'white_cards': "[]",
                'error': "Error" + + repr(ex)
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

##### Reviews

@api_view(['GET'])
def get_revs(request):
    if request.method == 'GET':
        reviewList = MamComment.objects.all().order_by('first_or_other')
        review_serializer = MamCommentSerializer(reviewList, many=True)
        response = {
            'message': "Get all reviews succefully",
            'wlists': review_serializer.data,
            'error': ''
        }
        return JsonResponse(review_serializer.data, safe=False)

@api_view(['POST'])
def create_rev(request):
    if request.method == 'POST':
        try: 
            review = JSONParser().parse(request)
            movie = MamMovie.objects.get(imdb_id = review['movie']['imdb_id'])
            autor = MamColaborator.objects.get(name = review['autor']['name'])
            review_serialized = MamCommentSerializer(data=review)
            if review_serialized.is_valid():
                #movie = MamMovie.objects.get(imdb_id = review_serialized.validated_data['movie']['imdb_id'])
                #autor = MamColaborator.objects.get(name = review_serialized.validated_data['autor']['name'])
                comment = MamComment(text = review_serialized.validated_data['text'],
                first_or_other =review_serialized.validated_data['first_or_other'],
                movie = movie,
                autor = autor)
                comment.save()
                cs = MamCommentSerializer(comment)
                return JsonResponse(cs.data, status=status.HTTP_201_CREATED)
            else:
                error = {
                    'message':"Can Not upload successfully!",
                    'wlits':"[]",
                    'error': review_serialized.errors
                    }
                return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(ex)
            exceptionError = {
                'message': "Can Not upload successfully!",
                'wlists': "[]",
                'error': "Having an exception! " + repr(ex)
                }
            return JsonResponse(exceptionError, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def delete_rev(request, pk):
    if request.method == 'DELETE':
        try:
            if MamComment.objects.filter(id=pk).exists():
                count = MamComment.objects.get(id=pk).delete()
            return JsonResponse({'message': '{} comment were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
        except Exception as ex:
            print(ex)
            error = {
                'message': "Fail! -> can NOT delete the entry. Please check again!",
                'white_cards': "[]",
                'error': "Error" + + repr(ex)
            }
            return JsonResponse(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)