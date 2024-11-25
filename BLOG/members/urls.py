from django.urls import reverse, path
from django.contrib.auth import views as auth_views
from .views import RegisterView, EditProfileForm, PassChangeView
from .views import PassChangeView
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from. import views


app_name = 'members'

urlpatterns =[
    path('register/', RegisterView.as_view(), name='register'),
    path('edit_profile', EditProfileForm.as_view(), name='edit_profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', PassChangeView.as_view(template_name='registration/change-password.html')),
    path('success', views.success, name="success"),

    #path('test_password_reset/', debug_view, name='password_reset'),
   
]

