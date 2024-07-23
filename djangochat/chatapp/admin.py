from django.contrib import admin
from chatapp.models import  Message, Chatroom

# Register your models here.

admin.site.register(Message)
admin.site.register(Chatroom)