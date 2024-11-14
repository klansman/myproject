from django import forms
from .models import Post, Category

#cats =[('coding','coding'), ('Blofs', 'Blofs'), ('Sports', 'Sports'),('News', 'News'),]
choices = Category.objects.all().values_list('catName','catName')
choices_list =[]

for item in choices:
    choices_list.append(item)

class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','body','category', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Post Title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id':'user', 'value':'', 'type':'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Share your idea', 'height':'200px'}),
            'category': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
                                     
        }
        