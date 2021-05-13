from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_videos, name='videos'),
    path('<video_id>', views.video_detail, name='video_detail'),
]
