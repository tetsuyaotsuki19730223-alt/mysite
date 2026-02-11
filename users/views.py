# users/views.py
import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .decorators import subscription_required

@subscription_required
def dashboard(request):
    return HttpResponse("🎉 課金ユーザー専用ページ")

# users/views.py
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

    event_type = event["type"]
    data = event["data"]["object"]

    # ✅ 課金完了
    if event_type == "checkout.session.completed":
        customer_id = data["customer"]
        profile = Profile.objects.get(stripe_customer_id=customer_id)
        profile.is_subscribed = True
        profile.current_price_id = settings.STRIPE_PRICE_ID
        profile.save()

    # 🚨 解約イベント（ここが④）
    if event_type == "customer.subscription.deleted":
        customer_id = data["customer"]
        profile = Profile.objects.get(stripe_customer_id=customer_id)
        profile.is_subscribed = False
        profile.current_price_id = None
        profile.save()

    return HttpResponse("ok")

def subscribe(request):
    import stripe
    from django.conf import settings
    from django.http import HttpResponse

    stripe.api_key = settings.STRIPE_SECRET_KEY

    session = stripe.checkout.Session.create(
        mode="subscription",
        line_items=[{
            "price": settings.STRIPE_PRICE_ID,
            "quantity": 1,
        }],
        metadata={
            "price_id": settings.STRIPE_PRICE_ID,
        },
        success_url="https://mysite-2-w9ja.onrender.com/success/",
        cancel_url="https://mysite-2-w9ja.onrender.com/cancel/",
    )

    return HttpResponse(f"REDIRECT:{session.url}")

# users/views.py
def success(request):
    return HttpResponse("SUCCESS OK")

def cancel(request):
    return HttpResponse("CANCELLED")

# users/views.py
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
        print("❌ WEBHOOK ERROR:", e)
        return HttpResponse(status=400)

    # =========================
    # 決済完了
    # =========================
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        print("✅ checkout.session.completed")

        # email からユーザー特定（まずはこれが一番簡単）
        email = session.get("customer_details", {}).get("email")

        if email:
            from django.contrib.auth.models import User
            from .models import Profile

            try:
                user = User.objects.get(email=email)
                profile = Profile.objects.get(user=user)
                profile.is_subscribed = True
                profile.current_price_id = settings.STRIPE_PRICE_ID
                profile.save()
                print("🎉 SUBSCRIPTION ON")
            except User.DoesNotExist:
                print("⚠️ User not found:", email)

    # =========================
    # 解約
    # =========================
    if event["type"] == "customer.subscription.deleted":
        subscription = event["data"]["object"]
        print("⚠️ subscription deleted")

        customer_id = subscription.get("customer")

        from .models import Profile

        try:
            profile = Profile.objects.get(stripe_customer_id=customer_id)
            profile.is_subscribed = False
            profile.current_price_id = None
            profile.save()
            print("🛑 SUBSCRIPTION OFF")
        except Profile.DoesNotExist:
            print("⚠️ Profile not found for customer:", customer_id)

    return HttpResponse("ok")
