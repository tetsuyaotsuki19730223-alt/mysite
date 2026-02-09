from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect

def subscribe(request):
    stripe_secret = getattr(settings, "STRIPE_SECRET_KEY", None)
    price_id = getattr(settings, "STRIPE_PRICE_ID", None)

    if not stripe_secret or not price_id:
        return HttpResponse(
            "Stripe is not configured",
            status=503
        )

    import stripe
    stripe.api_key = stripe_secret

    session = stripe.checkout.Session.create(
        mode="subscription",
        payment_method_types=["card"],
        line_items=[
            {
                "price": price_id,
                "quantity": 1,
            }
        ],
        success_url="https://mysite-admin.onrender.com/success/",
        cancel_url="https://mysite-admin.onrender.com/cancel/",
    )

    return redirect(session.url)
