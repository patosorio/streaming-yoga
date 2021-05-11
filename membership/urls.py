from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_memberships, name='memberships'),
    path('<subscription_type>', views.add_to_checkout, name="add_to_checkout"),
]