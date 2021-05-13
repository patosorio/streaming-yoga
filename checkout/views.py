import os
import stripe
import djstripe
import json
from django.conf import settings
from django.shortcuts import (
    render, redirect, reverse,
)
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from djstripe.models import Product


@login_required
def checkout(request):
    if request.method == 'POST':
        pass
    else:
        membership = 'monthly'
        membership = Product.objects.get(name="Monthly Subscription")
        if request.method == 'GET' and 'membership' in request.GET:
            if request.GET['membership'] == 'yearly':
                membership = 'yearly'
                membership = Product.objects.get(name="Yearly Subscription")

    template = 'checkout.html'
    context = {
        "membership": membership
    }

    return render(request, template, context)


def create_subscription(request):
    if request.method == "GET":
        pass
    else:
        print("hello")
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_TEST_SECRET_KEY
        stripe.api_key = stripe_secret_key
        """
            Create stripe customer and subscription and add them to the user object.
        """
        data = json.loads(request.data)

        email = data['email']
        assert request.user.email == email
        planId = data['planID']

        try:
            # Attach the payment method to the customer
            stripe.PaymentMethod.attach(
                data['paymentMethodId'],
                customer=data['customerId'],
            )
            # Set the default payment method on the customer
            customer = stripe.Customer.modify(
                data['customerId'],
                email=email,
                invoice_settings={
                    'default_payment_method': data['paymentMethodId'],
                },
            )

            djstripe_customer = djstripe.models.Customer.sync_from_stripe_data(customer)

            # Create the subscription
            subscription = stripe.Subscription.create(
                customer=data['customerId'],
                items=[
                    {
                        'plan': planId,
                    }
                ],
                expand=['latest_invoice.payment_intent'],
            )
            djstripe_subscription = djstripe.models.Subscription.sync_from_stripe_data(subscription)

            # associate customer and subscription with the user
            request.user.customer = djstripe_customer
            request.user.subscription = djstripe_subscription
            request.user.save()

            data = {
                'customer': customer,
                'subscription': subscription
            }
            return JsonResponse(
                data=data,
            )
        except Exception as e:
                return JsonResponse(error={'message': str(e)}), 200


# logic for customer & subscription following stripe subscription's model 
# https://stripe.com/docs/billing/subscriptions/fixed-price
