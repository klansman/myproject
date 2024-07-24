from django.shortcuts import render, redirect
from chatapp.models import Rooms, Message
from django.http import HttpResponse, JsonResponse
import logging

logger = logging.getLogger(__name__)
# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Rooms.objects.get(name=room)
    return render(request, 'room.html', {'room': room, 'username': username, 'room_details': room_details})

def checkroom(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Rooms.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Rooms.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)
    


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, room=room_id, user=username)
    new_message.save()
    return HttpResponse('message sent successfully')


def getMessages(request, room):
    room_details = Rooms.objects.get(name=room)

    message = Message.objects.filter(room=room_details.id)
    return JsonResponse({"message":list(message.values())})