from django.shortcuts import render, redirect
from .models import Chatroom, Message
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def checkroom(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Chatroom.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Chatroom.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
    
def room(request, room):
    username = request.GET.get('username')
    room_details = Chatroom.objects.get(name=room)
    return render(request, 'room.html', {'room': room, 'username': username, 'room_details': room_details})

def send(request):
    message = request.POST('message')
    username = request.POST.get('username')
    room_id = request.POST.get('room_id')
    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('message sent')

