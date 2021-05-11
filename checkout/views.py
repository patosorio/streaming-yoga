from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import OrderForm


def checkout(request):

    if request.method == 'POST':
        pass
    else:
        subscription = 'monthly'
        if request.method == 'GET' and 'subscription' in request.GET:
            if request.GET['subscription'] == 'yearly':
                subscription = 'yearly'
                print(subscription)
    
    order_form = OrderForm()
    template = 'checkout.html'
    context = {
        "order_form": order_form,
    }
    return render(request, template, context)
