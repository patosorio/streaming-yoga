from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from membership.models import Membership
from .models import Order, LineItem, Customer


def checkout(request):
    
    if request.method == 'POST':
        pass
    else:
        subscription = 'monthly'
        if request.method == 'GET' and 'subscription' in request.GET:
            if request.GET['subscription'] == 'yearly':
                subscription = 'yearly'
    
    print(subscription)
    membership = get_object_or_404(Membership, subscription_type=subscription)
    order_form = OrderForm()
    template = 'checkout.html'
    context = {
        "order_form": order_form,
        "membership": membership,
        "stripe_public_key": "pk_test_51ImzTfGFCpq2XfOb6Bpz00D7omwfZVYzsc48m2gCyuBWqCssVyl1aW5ZL6COJBXBTM6VSFRKNPJFEmm9QBJ7dfJQ00B9WvNlP6",
        "client_secret": "test client secret",
    }

    return render(request, template, context)
