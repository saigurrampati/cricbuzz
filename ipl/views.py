from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Team, Player, Match, Statistics
import datetime
from .form import TeamForm, PlayerForm, MatchForm


def home(request):
    return render(request, 'ipl/home.html', {})


def add_players(request):
    if request.method == "POST":
        print(request.POST)
        form = PlayerForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ipl/')
    else:
        form = PlayerForm()
        return render(request, 'ipl/add_players.html', {'form': form})


def players(request):
    player = Player.objects.all()
    return render(request, 'ipl/players.html', {'player': player})


def details(request, player_id):
    player_detail = Player.objects.get(player_id=player_id)
    return render(request, 'ipl/details.html', {'player_detail': player_detail})


