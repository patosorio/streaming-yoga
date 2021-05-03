from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    """ a View that renders the bag contents page """
    return render (request, 'checkout.html')


def add_to_checkout(request, membership_name):
    
    redirect_url = request.POST.get('redirect')
    membership_name = request.POST.get('membership_name')

    selected_membership = request.session.get('selected_membership', {})

