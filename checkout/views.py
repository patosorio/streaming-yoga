from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import OrderForm
from .models import Order, OrderLineItem, Customer
import stripe

def checkout(request, membership_type):

    order_form = OrderForm()
    template = "checkout.html"
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51ImzTfGFCpq2XfOb6Bpz00D7omwfZVYzsc48m2gCyuBWqCssVyl1aW5ZL6COJBXBTM6VSFRKNPJFEmm9QBJ7dfJQ00B9WvNlP6',
        'client_secret': "test secret client"
    }
    return render(request, template, context)


def pay(request):
    if membership_type != 'Monthly':
        membership_id = 'prod_JPpLp6Qm7n2H4F'
    else:
        membership_id = 'prod_JPpLoEcXPCvx31'
                
        session = stripe.checkout.Session.create(
            success_url="success?session_id={CHECKOUT_SESSION_ID}",
            cancel_url="cancel?session_id={CHECKOUT_SESSION_ID}",
            payment_method_types=["card"],
            line_items=[
                {
                    "price": membership_id,
                    "quantity": 1,
                },
            ],
            mode="subscription",
            client_reference_id=request.user,         
        )
        return render(request, 'checkout.html', {'session_id': session.id})  


def success(request):
    if request.method == 'GET' and 'session_id' in request.GET:
        session = stripe.checkout.Session.retrieve(request.GET['session_id'],)
        customer = Customer()
        customer.user = request.user
        customer.stripeid = session.customer
        customer.membership = True
        customer.cancel_at_period_end = False
        customer.stripe_subscription_id = session.subscription
        customer.save()
    return render(request, 'membership/success.html')