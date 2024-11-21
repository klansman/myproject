from django import forms
from .models import Post, Category

#this allows us to use the form fields directly in our html files instead of raw coding and using POST methods

choice = Category.objects.all().values_list('catName', 'catName')
choice_list = []

for items in choice:
    choice_list.append(items)

class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tag', 'body', 'author', 'category', 'body', 'header_image')
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'tag':forms.TextInput(attrs={'class': 'form-control'}),
            'body':forms.Textarea(attrs={'class': 'form-control'}),
            'author':forms.TextInput(attrs={'class': 'form-control', 'id': 'author', 'value': '', 'type': 'hidden'}),
            'category':forms.Select(choices=choice_list, attrs={'class': 'form-control'})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tag', 'body', 'header_image')
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'})
        }
