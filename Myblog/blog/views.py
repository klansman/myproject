from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Create your views here.
#def home(request): # function based view creation
   # post = Post.objects.all()
    #return render(request, 'home.html', {'post': post})

# Class based view creation
class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleView(DetailView):
    model = Post
    template_name = 'article_details.html'

class addPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'  # this allows for all the fields in the database to be present