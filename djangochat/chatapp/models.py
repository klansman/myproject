from django.db import models
from datetime import datetime

# Create your models here.
class Chatroom(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    value= models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)