from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home, name='home'),
    path('gallery/',views.gallery, name='gallery'),
    path('posts/<str:slug>/',views.detail, name='detail'),
    path('category/<str:slug>/',views.category, name='category'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)