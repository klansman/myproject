from django import forms
from .models import Post, Category

#this allows us to use the form fields directly in our html files instead of raw coding and using POST methods

choice = Category.objects.all().values_list('catName', 'catName')

class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tag', 'body', 'author', 'category', 'body')
        widgets = {
            'title':forms.Textarea(attrs={'class': 'form-control'}),
            'tag':forms.Textarea(attrs={'class': 'form-control'}),
            'body':forms.Textarea(attrs={'class': 'form-control'}),
            'author':forms.Select(attrs={'class': 'form-control'}),
            'category':forms.Select(attrs={'choices':'choice', 'class': 'form-control'})
        }