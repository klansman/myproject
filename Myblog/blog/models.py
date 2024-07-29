from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('article_details', args=(str(self.id))) #1
        #return reverse('home') #alternatively return to home page after creation.

    # What this function does is to route the url for any new post to the post itself by making use of the article_details class.
    #remember that the article details class takes in a dynamic parameter and this takes in the argument self.id, while self refers to the particular post
    #The reverse function from Django's urls module is used to generate the URL. 
    # The first argument to reverse is the name of the URL pattern defined in the Django project's URL configuration. 
    # In this case, 'article_details' is the name of the URL pattern that corresponds to the detail view of a single post. 
    