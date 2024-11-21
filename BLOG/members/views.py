from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import SignUpForm
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
    form_class = PasswordChangeForm
    success_url = reverse_lazy('login')
    template_name = 'registration/change-password.html'

    # def get(self, request, *args, **kwargs):
    #     print(f"PassChangeView called with template: {self.template_name}")
    #     return render(request, self.template_name)
    
    # def dispatch(self, *args, **kwargs):
    #     try:
    #         # Attempt to load the template
    #         template = get_template(self.template_name)
    #         print(f"Template found: {template.template.name}")
    #     except Exception as e:
    #         print(f"Error loading template: {e}")
    #     return super().dispatch(*args, **kwargs)


