from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('checkroom', views.checkroom, name='checkroom'),
    path('<str:room>/', views.room, name='room'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages')
]