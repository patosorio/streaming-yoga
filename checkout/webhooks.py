from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe
import json


@require_POST
@csrf_exempt
def webhook(request):
    """Listen for webhooks from Stripe"""

    #setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

    #get the webhook data and verify its signature
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
        json.loads(payload), wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Set up a webhook handler:
    handler = StripeWH_Handler(request)

    # Map webhook events to relevant handler function
    event_map = {
        'payment_intent.succeded': handler.handle_payment_intent_succeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
        'customer.created': handler.handle_customer_created,
        'customer.subscription.created': handler.handle_customer_subscription_created,
    }

    # Get the webhook type from Strip
    event_type = event['type']

    # If there's a handler for it, get it from the vent map
    # Use the generic one by default
    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event handler with the vent
    response = event_handler(event)
    return response