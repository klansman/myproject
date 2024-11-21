from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    body = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    category = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def get_absolute_url(self):
        return reverse('single', args=(str(self.id)))
    
    def total_likes(self):
        return self.likes.count()

class Category(models.Model):
    catName = models.CharField(max_length=255)

    def __str__(self):
        return self.catName
    


