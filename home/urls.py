from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('accounts/', include('allauth.urls')),
    path('videos/', include('videos.urls')),
]
