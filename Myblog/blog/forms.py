from django import forms
from .models import Post

class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Post title'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Share your idea'})
                                     
        }
