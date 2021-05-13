/* 

    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/billing/subscriptions/elements

    CSS from here:
    http://stripe.com/docs/stripe-js

*/

function createCustomer() {
    let billingEmail = document.querySelector('#email').value;
    return fetch('/checkout/create-customer', {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: billingEmail,
        }),
    })
    .then((response) => {
        return response.json();
    })
    .then((result) => {
        // result.customer.id is used to map back to the customer object
        return result;
    });
}

let stripe = Stripe("pk_test_51ImzTfGFCpq2XfOb6Bpz00D7omwfZVYzsc48m2gCyuBWqCssVyl1aW5ZL6COJBXBTM6VSFRKNPJFEmm9QBJ7dfJQ00B9WvNlP6");
let elements = stripe.elements();

let card = elements.create('card');
card.mount('#card-element');


/*
Use the test card number 4242 4242 4242 4242, 
any three-digit CVC number, any expiration date in the future, 
and any five-digit ZIP code.
*/

card.on('change', function (event) {
    let displayError = document.getElementById("card-errors");
    if (event.error) {
        var html = `<p>${event.error.message}</p>`
        $(displayError).html(html);     
    } else {
        displayError.textContent = '';
    }
});

// stripe-elements js function that validates user input as it is typed

function displayError(event) {
    changeLoadingStatePrices(false);
    let displayError = document.getElementById('card-element-errors');
    
}


// save payment details to create subscription in our backend

var form = document.getElementById('subscription-form');

form.addEventListener('submit', function (ev) {
  ev.preventDefault();
  createCustomer();
  createPaymentMethod(card);
});

function createPaymentMethod(card) {
    const customerId = result.customer.id;
    // Set up payment method for recurring usage
    let billingName = document.querySelector('#name').value;

    let planId = document.getElementById('planId').innerHTML;

    stripe
        .createPaymentMethod({
            type: 'card',
            card: card,
            billing_details: {
              name: billingName,
            },
        })
        .then((result) => {
            if (result.error) {
                displayError(result);
            } else {
                createSubscription({
                  customerId: customerId,
                  paymentMethodId: result.paymentMethod.id,
                  planId: planId,
                });
            }
        });
}

/* createSubscription Define function:
    passing: 
        customer
        payment method
        planId (priceId)
*/

function createSubscription(customerId, paymentMethodId, planId) {
    return (
        fetch('/create_subscription', {
            method: 'post',
            headers: {
              'Content-type': 'application/json',
            },
            body: JSON.stringify({
              customerId: customerId,
              paymentMethodId: paymentMethodId,
              planId: planId,
            }),
        })
        .then((response) => {
            return response.json();
        })
        // If the card is declined, display an error to the user.
        .then((result) => {
            if (result.error) {
                // The card had an error when trying to attach it to a customer.
                throw result;
            }
            return result;
        })
        // Normalize the result to contain the object returned by Stripe.
        // Add the additional details we need.
        .then((result) => {
            return {
                paymentMethodId: paymentMethodId,
                planId: planId,
                subscription: result,
            };
        })
        // Some payment methods require a customer to be on session
        // to complete the payment process. Check the status of the
        // payment intent to handle these actions.
        .then(handlePaymentThatRequiresCustomerAction)
        // If attaching this card to a Customer object succeeds,
        // but attempts to charge the customer fail, you
        // get a requires_payment_method error.
        .then(handleRequiresPaymentMethod)
        // No more actions required. Provision your service for the user.
        .then(onSubscriptionComplete)
        .catch((error) => {
          // An error has happened. Display the failure to the user here.
          // We utilize the HTML element we created.
          showCardError(error);
        })
    );
}

/*
  Verify the subscription status is active
  check the product customer subscribed to and grant access to the video service
*/





