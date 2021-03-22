from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *


# Create your views here.


def home(request):
    if request.method == "POST":
        username = request.POST.get('username')
        option = request.POST.get('option')
        room_code = request.POST.get('room_code')

        # if user selects option 1 it means they have an existing room_code from the opponent
        if option == '1':
            game = Game.objects.filter(room_code=room_code).first()

            # both room_codes must be similar, otherwise the opponent will not join player1
            if game is None:
                messages.success(request, "Room code not found")
                return redirect('/')

            if game.is_over:
                messages.success(request, "Game is over")
                return redirect('/')

            # game opponent also uses username to have access to the game
            game.game_opponent = username
            game.save()
        else:

            # player1 must create a new room_code
            game = Game(game_creator=username, room_code=room_code)
            game.save()
            return redirect('/play/' + room_code + '?username=' + username)

    return render(request, 'tictactoe/home.html')


def play(request, room_code):
    username = request.GET.get('username')
    context = {'room_code': room_code, 'username': username}
    return render(request, 'tictactoe/play.html', context)
