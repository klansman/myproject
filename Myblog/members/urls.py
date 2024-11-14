from django.urls import path
from .views import registerView, UserEditView, PassChangeView
from .import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('register', registerView.as_view(), name='register'), #function based view
    path('edit_profile', UserEditView.as_view(), name='edit_profile'),
    path('password/', PassChangeView.as_view(), name='changePassword'),
    path('success', views.success, name='success'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    
]