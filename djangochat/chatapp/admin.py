from django.contrib import admin
from chatapp.models import  Message, Chatrooms

# Register your models here.

admin.site.register(Message)
admin.site.register(Chatrooms)