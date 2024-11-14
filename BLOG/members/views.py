from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import SignUpForm
from django.urls import reverse_lazy

# Create your views here.
class RegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'members/templates/registration/register.html'
    success_url = reverse_lazy('login')   
    #context_object_name = 'register' 

class EditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name ='members/registration/edit.html'
    success_url = reverse_lazy('login')

    def get_object(self): #necessary for making sure that the curent user is logged in before having to edit profile
        return self.request.user
