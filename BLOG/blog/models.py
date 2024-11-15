from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    category = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('single', args=(str(self.id)))

class Category(models.Model):
    catName = models.CharField(max_length=255)

    def __str__(self):
        return self.catName

