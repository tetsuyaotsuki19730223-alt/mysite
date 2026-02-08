import json
import stripe

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from users.models import Profile


def subscribe(request):
    return HttpResponse("subscribe OK")


# payments/views.py

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

    try:
        event = stripe.Webhook.construct_event(
            payload=payload,
            sig_header=sig_header,
            secret=settings.STRIPE_WEBHOOK_SECRET,
        )
    except Exception as e:
        print("❌ Webhook error:", e)
        return HttpResponse(status=400)

    print("📦 event type:", event["type"])

    # ✅ 購読開始
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        customer_id = session.get("customer")
        subscription_id = session.get("subscription")

        profile = Profile.objects.get(user__username="admin")
        profile.is_subscribed = True
        profile.stripe_customer_id = customer_id
        profile.stripe_subscription_id = subscription_id
        profile.save()

        print("✅ subscription activated")

    # 🔥 ここが追加（超重要）
    if event["type"] == "customer.subscription.deleted":
        subscription = event["data"]["object"]
        subscription_id = subscription["id"]

        profile = Profile.objects.get(
            stripe_subscription_id=subscription_id
        )
        profile.is_subscribed = False
        profile.stripe_subscription_id = None
        profile.save()

        print("🔒 subscription canceled")

    return HttpResponse(status=200)
