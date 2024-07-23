from django.shortcuts import render, redirect
from .models import Chatrooms, Message
from django.http import HttpResponse, JsonResponse
import logging

logger = logging.getLogger(__name__)
# Create your views here.
def home(request):
    return render(request, 'home.html')

def checkroom(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Chatrooms.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Chatrooms.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
    
def room(request, room):
    username = request.GET.get('username')
    room_details = Chatrooms.objects.get(name=room)
    return render(request, 'room.html', {'room': room, 'username': username, 'room_details': room_details})

def send(request):
    message = request.POST('message')
    username = request.POST.get('username')
    room_id = request.POST.get('room_id')
    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    logger.info(f'received new message: {username}, username: {username}, room_id: {room_id}')
    return HttpResponse('message sent')

def getMessages(request, room):
    room_details = Chatrooms.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({'message':list(messages.values())})