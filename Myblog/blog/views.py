from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForms
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
#def home(request): # function based view creation
   # post = Post.objects.all()
    #return render(request, 'home.html', {'post': post})

# Class based view creation

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['created']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"]= cat_menu
        return (context)

def CatView(request, cats):
    for category in Category.objects.all():
        category.catName=category.catName.lower()
        category.save()
    cats = cats.lower()
    if not Category.objects.filter(catName=cats.replace('-', ' ')).exists():
        return HttpResponse("Category not found", status=404)
    cat_post = Post.objects.filter(category__iexact = cats.replace('-', ' '))
    if not cat_post.exists():
        return HttpResponse("No posts found in this Category", status=404)
    return render(request, 'category.html', {'cat_post':cat_post, 'cats': cats.title().replace('-', ' ')})
    
def catListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu': cat_menu_list})

def likeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    #post.likes.add(request.user)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article_details', args = [str(pk)]))

class ArticleView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cont = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = cont.total_likes()
        context = super(ArticleView, self).get_context_data(*args, **kwargs)
        context["total_likes"]= total_likes
        liked = False
        if cont.likes.filter(id=self.request.user.id).exists():
            liked = True
            context["liked"] = liked
        return context

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

class addCatView(CreateView):
    model = Category
    #form_class = PostForms
    fields = '__all__'
    template_name = 'add_category.html'
    success_url = reverse_lazy('home')



