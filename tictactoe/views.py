from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from tictactoe.models import Game


# Create your views here.


def home(request):
    if request.method == "POST":
        username = request.POST.get('username')
        option = request.POST.get('option')
        room_code = request.POST.get('room_code')

        # check if the user selected 1st or second option
        if option == '1':
            game = Game.objects.filter(room_code=room_code).first()

            # If the game-opponent inputs room-code that is not similar to the game_creator - Error occurs with msg
            if game is None:
                messages.success(request, "Room code not found")
                return redirect('/')

            if game.is_over:
                messages.success(request, "Game is over")
                return redirect('/')

            game.game_opponent = username
            game.save()
        else:
            game = Game(game_creator=username, room_code=room_code)
            game.save()
            return redirect('/play/' + room_code + '?username=' + username)

    return render(request, "tictactoe/home.html")


def play(request, room_code):
    username = request.GET.get('username')
    results = Game.objects.all()
    paginator = Paginator(results, 3)
    page = request.GET.get('page')
    results = paginator.get_page(page)

    context = {'room_code': room_code, 'username': username, "Game": results}

    return render(request, "tictactoe/play.html", context)
