import json
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

@csrf_exempt
def stripe_webhook(request):
    # Stripe 無効なら何もしない（admin保護）
    if not settings.STRIPE_ENABLED:
        return HttpResponse(status=200)

    try:
        import stripe
        stripe.api_key = settings.STRIPE_SECRET_KEY
    except ImportError:
        return HttpResponse(status=200)

    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except Exception:
        # 署名エラーでも 200 を返す（Stripe再送防止）
        return HttpResponse(status=200)

    # 🔔 イベント処理
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]

        handle_checkout_completed(session)

    return HttpResponse(status=200)

User = get_user_model()

def handle_checkout_completed(session):
    """
    支払い完了時の処理
    """
    customer_id = session.get("customer")
    email = session.get("customer_details", {}).get("email")

    if not email:
        return

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return

    # 例：Profile がある場合
    profile = getattr(user, "profile", None)
    if profile:
        profile.is_subscribed = True
        profile.stripe_customer_id = customer_id
        profile.save()

def create_checkout_session(request):
    return HttpResponse("OK subscribe") 