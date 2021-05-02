from django.shortcuts import render
from .models import Video

# Create your views here.

def all_videos(request):
    """ A view to show all products, including sorting and search queries """

    videos = Video.objects.all()

    context = {
        'videos': videos,
    }

    return render(request, 'videos.html', context)