from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('gallery/',views.gallery, name='gallery'),
    path('posts/all/',views.posts, name='posts'),
    path('posts/<str:slug>/',views.detail, name='detail'),
    path('category/<str:slug>/',views.category, name='category'),
    path('tag/<str:slug>/', views.tagView,name='tagpost' ),
]
