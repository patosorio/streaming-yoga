/* 

    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/billing/subscriptions/elements

    CSS from here:
    http://stripe.com/docs/stripe-js

*/
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


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
    let displayError = document.getElementById('card-element-errors');
    console.log(event);
}


function planSelect(name, price, priceId) {
    var inputs = document.getElementsByTagName('input');
    // loop over the inputs and find one that has same name value
    for(var i = 0; i<inputs.length; i++){
      inputs[i].checked = false;
      if(inputs[i].name== name){

        inputs[i].checked = true;
      }
    }

    var n = document.getElementById('plan');
    var p = document.getElementById('price');
    var pid = document.getElementById('priceId');
    n.innerHTML = name;
    p.innerHTML = price;
    pid.innerHTML = priceId;
        document.getElementById("subscribe").disabled = false;
}

let paymentForm = document.getElementById('subscription-form');
    if (paymentForm) {
        paymentForm.addEventListener('submit', function (evt) {
            evt.preventDefault();
            card.update({ 'disabled': true});
            $().attr('#subscribe').attr('disabled', true)
            // create new payment method & create subscription
            createPaymentMethod({ card });
        });
    }

function createPaymentMethod({ card }) {
// Set up payment method for recurring usage
    let billingName = '{{user.username}}';

    stripe
        .createPaymentMethod({
            type: 'card',
            card: card,
            billing_details: {
                name: billingName,
            },
        }).then((result) => {
            if (result.error) {
                displayError(result);
            } else {
                const paymentParams = {
                price_id: document.getElementById("priceId").innerHTML,
                payment_method: result.paymentMethod.id,
        };
        
        fetch("/checkout/create_subscription", {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
            },
            credentials: 'same-origin',
            body: JSON.stringify(paymentParams),
        }).then((response) => {
            return response.json(); 
        }).then((result) => {
            if (result.error) {
            // The card had an error when trying to attach it to a customer
                throw result;
            }
            return result;
        }).then((result) => {
            if (result && result.status === 'active') {
                window.location.href = '/complete';
            };
        }).catch(function (error) {
            displayError(error);
        });
        }
        });
}
  