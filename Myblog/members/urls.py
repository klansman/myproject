from django.urls import path
from .views import registerView, UserEditView

urlpatterns=[
    path('register', registerView.as_view(), name='register'), #function based view
    path('edit_profile', UserEditView.as_view(), name='edit_profile'),
]