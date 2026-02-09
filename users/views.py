from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.shortcuts import redirect


@csrf_exempt
def stripe_webhook(request):
    return HttpResponse("ok")


def subscribe(request):
    try:
        import stripe
    except ImportError:
        return HttpResponse("Stripe not installed", status=500)

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
        success_url="http://mysite-admin.onrender.com/success/",
        cancel_url="http://mysite-admin.onrender.com/cancel/",
    )

    return redirect(session.url)
