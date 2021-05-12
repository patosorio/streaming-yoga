from django.shortcuts import render, redirect, reverse, HttpResponse
from .models import Membership
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


# Create your views here.
def all_memberships(request):
    """ a view to return membership page """
    memberships = Membership.objects.all()
    context = {
        'memberships': memberships,
    }
    return render(request, "memberships.html", context)


