from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    #email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'class':'required'}))
    #first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'class':'required'}))
    #last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'class':'required'}))

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'



