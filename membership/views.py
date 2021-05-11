from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
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


def add_to_checkout(request, subscription_type):

    membership = get_object_or_404(Membership, subscription_type=subscription_type)

    print(membership)

    context = {"membership": membership}

    return render(request, 'checkout.html', context)


"""
def add_to_checkout(request, membership_id):
    print("something")
    membership = get_object_or_404(Membership)
    context = {
        "membership_id": membership.id
    }
    return render(request, "memberships.html", context)


    membership = get_object_or_404(Membership, membership_id=membership.id) 
    cart = request.session.get('cart', {})
    cart = membership
    request.session['cart'] = cart
    print(request.session['cart'])
"""