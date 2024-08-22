from django.urls import path
# from . import views  # function based
from .views import HomeView, ArticleView, addPostView, editPostView, deletePostView, addCatView, CatView, catListView, likeView
from . import views

urlpatterns=[
    #path('', views.home, name='home'), #function based view
    path('', HomeView.as_view(), name='home'), #class based view 
    path('article/<str:pk>', ArticleView.as_view(), name='article_details'), #dynamic view with pk set as an integer
    path('add_post/', addPostView.as_view(), name='add_post'),
    path('article/edit_post/<str:pk>', editPostView.as_view(), name='edit_post'),
    path('article/<str:pk>/delete', deletePostView.as_view(), name='delete_post'),
    path('add_category/', addCatView.as_view(), name='add_category'),
    path('category/<str:cats>/', CatView, name='category'),
    path('category_list', catListView, name='category_list'),
    path('like/<str:pk>', likeView, name='like_post'),
]