from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import SignUpForm, PassChangingForm
from django.urls import reverse_lazy
from django.template.loader import get_template
from django.http import HttpResponse
# Create your views here.
class RegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'members/templates/registration/register.html'
    success_url = reverse_lazy('login')   
    #context_object_name = 'register' 

class EditProfileForm(generic.UpdateView):
    form_class = UserChangeForm
    template_name ='members/templates/registration/edit_profile.html'
    success_url = reverse_lazy('login')

    def get_object(self): #necessary for making sure that the curent user is logged in before having to edit profile
        return self.request.user


class PassChangeView(PasswordChangeView):
    form_class = PassChangingForm
    success_url = reverse_lazy('success')
    template_name = 'registration/change-password.html'

def success(request):
    return render(request, 'members/templates/registration/success.html')

