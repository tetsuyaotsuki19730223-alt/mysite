from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect


def get_stripe():
    if not settings.STRIPE_ENABLED:
        return None

    try:
        import stripe
        stripe.api_key = settings.STRIPE_SECRET_KEY
        return stripe
    except ImportError:
        return None


def subscribe(request):
    stripe = get_stripe()
    if stripe is None:
        return HttpResponse("Stripe is not configured", status=503)

    session = stripe.checkout.Session.create(
        mode="subscription",
        payment_method_types=["card"],
        line_items=[
            {
                "price": settings.STRIPE_PRICE_ID,
                "quantity": 1,
            }
        ],
        success_url=request.build_absolute_uri("/subscribe/success/"),
        cancel_url=request.build_absolute_uri("/subscribe/cancel/"),
    )

    return redirect(session.url)
