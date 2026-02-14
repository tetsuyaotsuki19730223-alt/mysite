import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import Profile


# =========================
# Subscribe (Checkout開始)
# =========================
@login_required
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
        metadata={
            "user_id": request.user.id,
        },
    )

    return HttpResponse(f"REDIRECT:{session.url}")


# =========================
# Webhook
# =========================
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
    if event["type"] in [
            "checkout.session.completed",
            "invoice.payment_succeeded",
            "customer.subscription.created"
        ]:
        print("🔥 EVENT TYPE:", event["type"])
        session = event["data"]["object"]

        email = session.get("customer_email")

    if email:
        from django.contrib.auth.models import User
        from .models import Profile

        try:
            user = User.objects.get(email=email)
            profile, _ = Profile.objects.get_or_create(user=user)
            profile.is_subscribed = True
            profile.current_price_id = settings.STRIPE_PRICE_ID
            profile.save()

            print("🎉 SUBSCRIPTION ON")

        except User.DoesNotExist:
            print("⚠️ User not found:", email)

    return HttpResponse("ok")


# =========================
# 成功・キャンセル
# =========================
@login_required
def success(request):
    return HttpResponse("SUCCESS OK")


@login_required
def cancel(request):
    return HttpResponse("CANCELLED")


# =========================
# プレミアムページ
# =========================
@login_required
def premium(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if not profile.is_subscribed:
        return redirect("subscribe")

    return HttpResponse("🔥 PREMIUM CONTENT 🔥")