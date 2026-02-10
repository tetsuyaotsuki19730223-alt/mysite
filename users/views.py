import stripe
from django.conf import settings
from django.shortcuts import redirect

stripe.api_key = settings.STRIPE_SECRET_KEY

def subscribe(request):
    session = stripe.checkout.Session.create(
        mode="subscription",   # ← 絶対必要
        payment_method_types=["card"],
        line_items=[{
            "price": settings.STRIPE_PRICE_ID,  # price_から始まるID
            "quantity": 1,
        }],
        success_url="https://mysite-2-w9ja.onrender.com/success/",
        cancel_url="https://mysite-2-w9ja.onrender.com/cancel/",
    )

    return redirect(session.url)
