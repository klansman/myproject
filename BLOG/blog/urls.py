from django.urls import reverse, path
from .views import indexView, catView, singleView, testview

urlpatterns =[
    path('', indexView.as_view(), name='index'),
    path('category/<str:cats>/', catView, name='category'),
    path('single/<str:pk>/', singleView.as_view(), name='single'),
    path('test/', testview, name='test'),
]