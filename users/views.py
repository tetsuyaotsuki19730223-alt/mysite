from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect

def subscribe(request):
    # 念のためのガード
    if not settings.STRIPE_ENABLED:
        return HttpResponse("Stripe is disabled", status=503)

    import stripe
    stripe.api_key = settings.STRIPE_SECRET_KEY

    session = stripe.checkout.Session.create(
        mode="subscription",
        payment_method_types=["card"],
        line_items=[
            {
                "price": settings.STRIPE_PRICE_ID,
                "quantity": 1,
            }
        ],
        success_url="https://mysite-2-w9ja.onrender.com/success/",
        cancel_url="https://mysite-2-w9ja.onrender.com/cancel/",
    )

    return redirect(session.url, code=303)


def success(request):
    return HttpResponse(
        "<h1>支払いが完了しました 🎉</h1>"
    )


def cancel(request):
    return HttpResponse(
        "<h1>支払いはキャンセルされました</h1>"
    )
