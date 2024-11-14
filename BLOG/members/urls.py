from django.urls import reverse, path
from django.contrib.auth import views as auth_views
from .views import RegisterView, EditView

app_name = 'members'

urlpatterns =[
    path('register/', RegisterView.as_view(), name='register'),
    path('edit_profile', EditView.as_view(), name='edit_profile'),
    #path('login', EditView.as_view(), name='login')
   
]

