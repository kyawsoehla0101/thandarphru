from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('tdp-admin-tdp/', admin.site.urls),
    path('',include('base.urls')),
    path('summernote/', include('django_summernote.urls')),
]
