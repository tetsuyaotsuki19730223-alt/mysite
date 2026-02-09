from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect

def create_checkout_session(request):
    return HttpResponse("STRIPE VIEW ACTIVE")


def create_checkout_session(request):
    stripe = get_stripe()
    if stripe is None:
        return HttpResponse("Stripe is disabled", status=503)

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="subscription",
        line_items=[
            {
                "price": "price_xxxxxxxxx",  # ← Test mode の Price ID
                "quantity": 1,
            }
        ],
        success_url="https://mysite-admin.onrender.com/success/",
        cancel_url="https://mysite-admin.onrender.com/cancel/",
    )

    return redirect(session.url)
