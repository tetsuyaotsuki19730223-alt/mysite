from django.conf import settings
from django.http import HttpResponse
import stripe

def subscribe(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    session = stripe.checkout.Session.create(
        mode="subscription",
        line_items=[{
            "price": settings.STRIPE_PRICE_ID,
            "quantity": 1,
        }],
        success_url=request.build_absolute_uri("/success/"),
        cancel_url=request.build_absolute_uri("/cancel/"),
    )

    return HttpResponse(f"REDIRECT:{session.url}")
