from random import choice
from django.shortcuts import render
from .instances import dictionary
from django.contrib import messages

def home(request):  
    return render(request, 'home.html', {})

def play(request, option):
    options = ['rock', 'paper', 'scissors', 'spock', 'lizard']
    opponent = choice(options)
    instance_player = dictionary[option]
    instance_opponent = dictionary[opponent]
    if instance_player > instance_opponent:
        messages.add_message(request, messages.INFO, 'You won!')
    elif instance_opponent > instance_player:
        messages.add_message(request, messages.INFO, 'You lost!')
    elif instance_opponent == instance_player:
        messages.add_message(request, messages.INFO, 'You tied!')
    return render(request, 'play.html', {'option':option, 'opponent':opponent})