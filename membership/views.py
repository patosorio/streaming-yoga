from django.shortcuts import render
from django.views.generic import ListView
from .models import Membership
# Create your views here.


def all_memberships(request):

    memberships = Membership.objects.all()

    context = {
        'memberships': memberships,
    }

    return render(request, 'memberships.html', context)
