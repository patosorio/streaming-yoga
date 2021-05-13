from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    """ a view to return index page """
    if request.user.is_authenticated:
        return redirect("videos")
    return render(request, "home/index.html")
