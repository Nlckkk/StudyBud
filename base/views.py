from django.shortcuts import render, redirect
from django.contrib import messages 
from .models import Room
from django.db.models import Q
from django.contrib.auth.models import User
from .forms import RoomForm

# Create your views here.

#rooms = [
#    {'id': 1, 'name':'Lets learn python!'},
#    {'id': 2, 'name':'Design with me'},
#    {'id': 3, 'name':'Front end developer'},
#]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms' : rooms}
    return render(request, 'base/home.html', {'rooms':rooms})

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}

    return render(request, 'base/room.html',context)