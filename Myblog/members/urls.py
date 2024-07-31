from django.urls import path
from .views import registerView

urlpatterns=[
    path('register', registerView.as_view(), name='register'), #function based view
]