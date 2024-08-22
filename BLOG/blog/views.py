from django.shortcuts import render, HttpResponse
from .models import Post , Category
from django.views.generic import ListView, DeleteView, DetailView
from django.db.models import Count

# Create your views here.
class indexView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-created_at']

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


def testview(request):
    all = Category.objects.all()
    return render(request, 'test.html', {'all':all})

   