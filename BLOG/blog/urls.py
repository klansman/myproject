from django.urls import reverse, path
from .views import indexView, catView, singleView, testview, addPostView, updateView, deletePostView, likeView

urlpatterns =[
    path('', indexView.as_view(), name='index'),
    path('category/<str:cats>/', catView, name='category'),
    path('single/<int:pk>/', singleView.as_view(), name='single'),
    path('test/', testview, name='test'),
    path('addPost/', addPostView.as_view(), name='addPost'),
    path('single/update/<str:pk>', updateView.as_view(), name='update'),
    path('single/<int:pk>/delete', deletePostView.as_view(), name='delete'),
    path('like/<str:pk>', likeView, name='like_post'),
]