from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Video, Category
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def all_videos(request):
    """ A view to show all videos, including sorting and search queries """

    videos = Video.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                videos = videos.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            videos = videos.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            videos = videos.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter search criteria")
                return redirect(reverse('videos'))
            
            queries = Q(title__icontains=query) | Q(description__icontains=query)
            videos = videos.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'videos': videos,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'videos.html', context)


def video_detail(request, video_id):
    """ A view to show the video detail """

    video = get_object_or_404(Video, id=video_id)

    context = {"video": video}

    return render(request, 'video_detail.html', context)
