from django.urls import path
# from . import views  # function based
from .views import HomeView, ArticleView, addPostView

urlpatterns=[
    #path('', views.home, name='home'), #function based view
    path('', HomeView.as_view(), name='home'), #class based view 
    path('article/<str:pk>', ArticleView.as_view(), name='article_details'), #dynamic view with pk set as an integer
    path('add_post/', addPostView.as_view(), name='add_post'),
]