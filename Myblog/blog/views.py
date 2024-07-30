from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForms
from django.urls import reverse_lazy

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
    form_class = PostForms
    template_name = 'add_post.html'

    #fields = '__all__'  # this allows for all the fields in the database to be present, or you can just specify which fields you want

class editPostView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    form_class = PostForms
   # fields = ['title', 'body']

class deletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home') #this is where the url is redirected to after successful delete