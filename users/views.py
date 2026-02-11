from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import stripe


def subscribe(request):
    # 念のためガード
    if not settings.STRIPE_ENABLED:
        return HttpResponse("Stripe disabled", status=503)

    stripe.api_key = settings.STRIPE_SECRET_KEY

    session = stripe.checkout.Session.create(
        mode="subscription",
        line_items=[
            {
                "price": settings.STRIPE_PRICE_ID,
                "quantity": 1,
            }
        ],
        success_url=request.build_absolute_uri("/success/"),
        cancel_url=request.build_absolute_uri("/cancel/"),
    )

    # Stripe公式推奨：リダイレクト
    return HttpResponseRedirect(session.url)


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

    print("🔥 WEBHOOK HIT")  # ← これ入れて！

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.STRIPE_WEBHOOK_SECRET,
        )
    except Exception as e:
        print("❌ WEBHOOK ERROR:", e)
        return HttpResponse(str(e), status=400)

    if event["type"] == "checkout.session.completed":
        print("✅ checkout.session.completed received")

    return HttpResponse("ok", status=200)
