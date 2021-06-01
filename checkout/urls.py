from django.contrib import admin
from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('create_subscription', views.create_subscription, name='create_subscription'),
    path('wh/', webhook, name='webhook'),
]
