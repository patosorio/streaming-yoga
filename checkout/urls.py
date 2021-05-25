from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('create_subscription', views.create_subscription, name='create_subscription'),
]