from django.shortcuts import render, redirect, reverse, HttpResponse
from .models import Membership
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from djstripe.models import Product
# Create your views here.

@login_required
def all_memberships(request):
    """ a view to return membership page """
    memberships = Product.objects.all()
    context = {
        'memberships': memberships,
    }
    return render(request, "memberships.html", context)