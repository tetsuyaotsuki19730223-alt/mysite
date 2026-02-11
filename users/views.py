from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
import stripe

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.STRIPE_WEBHOOK_SECRET,
        )
    except Exception as e:
        return HttpResponse(str(e), status=400)

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        print("✅ checkout.session.completed:", session["id"])
        # 👉 ここでユーザーを「購読中」にする（後で）

    return HttpResponse("ok")
