import stripe
import djstripe
import json
from django.conf import settings
from django.shortcuts import (
    render, redirect, reverse,
)
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from djstripe.models import Product, Customer, Subscription


@login_required
def checkout(request):

    membership = Product.objects.all()

    template = 'checkout.html'
    context = {
        "membership": membership
    }

    return render(request, template, context)


# logic for customer & subscription following stripe subscription's model 
# https://stripe.com/docs/billing/subscriptions/fixed-price

@login_required
def create_subscription(request):
    if request.method == 'GET':
        pass
    else:
        # Reads application/json and returns a response

        data = json.loads(request.body)
        payment_method = data['payment_method']
        stripe.api_key = djstripe.settings.STRIPE_TEST_SECRET_KEY

        payment_method_obj = stripe.PaymentMethod.retrieve(payment_method)
        djstripe.models.PaymentMethod.sync_from_stripe_data(payment_method_obj)
        print("post")
        # create a new customer to attach to the user later

        try:
            customer = stripe.Customer.create(
                payment_method=payment_method,
                email=request.user.email,
                invoice_settings={
                    'default_payment_method': payment_method
                }
            )
            print(customer)
            djstripe_customer = djstripe.models.Customer.sync_from_stripe_data(customer)
            request.user.customer = djstripe_customer

            subscription = stripe.Subscription.create(
                customer=customer.id,
                items=[
                    {
                        "price": data["price_id"],
                    },
                ],
                expand=["latest_invoice.payment_intent"]
            )
            print(subscription)
            djstripe_subscription = djstripe.models.Subscription.sync_from_stripe_data(subscription)
            request.user.subscription = djstripe_subscription
          
            request.user.save()

            return JsonResponse(subscription)
        except Exception as e:
            return JsonResponse({'error': (e.args[0])}, status=403)

        print("Success")
        return HttpResponse(status=200)