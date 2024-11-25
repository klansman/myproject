from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.CharField(max_length=255, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile_pic")
    insta_url = models.URLField(null=True, blank=True, max_length=255)
    linkedin_url = models.URLField(null=True, blank=True, max_length=255)
    facebook_url = models.URLField(null=True, blank=True, max_length=255)
    twitter_url = models.URLField(null=True, blank=True, max_length=255)

    def __str__(self):
        return str(self.user)
    
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
    


