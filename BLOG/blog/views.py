from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post , Category
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from django.db.models import Count
from django.urls import reverse_lazy, reverse
from .forms import PostForms, EditForm
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


# Create your views here.
class indexView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-created_at'] #ordering post by created newest first

    
   # def get_context_data(self, **kwargs):# get the default context from the ListView
       # context=super().get_context_data(**kwargs) # Retrieve the third to last post
        #posts = Post.objects.order_by('-created_at')

        #post_1 = posts[0] if len(posts) > 0 else None
        #post_2 = posts[1] if len(posts) > 0 else None
        #post_3 = posts[2] if len(posts) > 0 else None
        #post_4 = posts[3] if len(posts) > 0 else None
        #post_5 = posts[4] if len(posts) > 0 else None
        
        #context['post_1'] = post_1
        #context['post_2'] = post_2
        #context['post_3'] = post_3
        #context['post_4'] = post_4
        #context['post_5'] = post_5
        
        #return (context)

        #a more efficient and clean way
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Retrieve posts ordered by created_at (assuming `Post` has a `created_at` field)
        posts = Post.objects.order_by('-created_at')
        
        # Store posts in a dictionary with keys 'post_1', 'post_2', etc.
        post_dict = {}
        for i in range(5):  # Adjust the range if you want more or fewer posts
            post_dict[f'post_{i + 1}'] = posts[i] if len(posts) > i else None
        
        # Add post_dict to the context
        context.update(post_dict)
        
        return context

            
def catView(request, cats):
    all_cats = Category.objects.annotate(post_count=Count('catName'))
    for category in Category.objects.all():
        category.catName = category.catName.lower()
        category.save()
    cats = cats.lower()
    
    
    if not Category.objects.filter(catName=cats).exists():
        return HttpResponse("Category not found", status=404)
    cat_post = Post.objects.filter(category__iexact=cats)
    
    if not cat_post.exists():
        return HttpResponse("No post in category", status=404)
    return render(request, 'category.html', {'cat_post':cat_post, 'cats':cats, 'all_cats':all_cats})

class singleView(DetailView):
    model = Post
    template_name = 'single.html'
    context_object_name = 'post' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        paragraphs = post.body.split('\n')
        context['first_part'] = paragraphs[:3]
        context['remaining_part'] = paragraphs[3:]
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Retrieve the posts ordered by `created_at` (assuming `Post` has a `created_at` field)
        posts = Post.objects.order_by('-created_at')[:4]  # Get the latest 5 posts
        
        # Pass the list of posts to the context
        context['posts'] = posts
        
        return context
    def get_context_data(self, *args, **kwargs):
        count = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = count.total_likes()
        liked = False
        if count.likes.filter(id=self.request.user.id).exists():
            liked = True
        context = super(singleView, self).get_context_data(*args, **kwargs)
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


def testview(request):
    all = Category.objects.all()
    posts = Post.objects.order_by('-created_at')
    title = posts[2] if len(posts) > 2 else None
    print ("Third Post:", title.title)
    
    return render(request, 'test.html', {'all':all, 'title':title})

class addPostView(CreateView):
    model = Post
    form_class = PostForms
    template_name = 'addPost.html'
    #fields = '__all__'

class updateView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update.html'

class deletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('index')

def likeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user.id)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
   
    return HttpResponseRedirect(reverse('single', args=[str(pk)]))

