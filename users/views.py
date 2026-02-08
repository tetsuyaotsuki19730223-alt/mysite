import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Profile

stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
@require_POST
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.STRIPE_WEBHOOK_SECRET
        )
    except Exception:
        return HttpResponse(status=400)

    data = event["data"]["object"]

    if event["type"] in (
        "customer.subscription.created",
        "customer.subscription.updated",
    ):
        _activate_subscription(data)

    if event["type"] == "customer.subscription.deleted":
        _deactivate_subscription(data)

    return HttpResponse(status=200)


def _activate_subscription(data):
    customer_id = data["customer"]
    subscription_id = data["id"]
    status = data["status"]

    if status not in ("active", "trialing"):
        return

    try:
        profile = Profile.objects.get(stripe_customer_id=customer_id)
    except Profile.DoesNotExist:
        return

    profile.is_subscribed = True
    profile.stripe_subscription_id = subscription_id
    profile.save()


def _deactivate_subscription(data):
    customer_id = data["customer"]

    try:
        profile = Profile.objects.get(stripe_customer_id=customer_id)
    except Profile.DoesNotExist:
        return

    profile.is_subscribed = False
    profile.stripe_subscription_id = None
    profile.save()


@login_required
def create_checkout_session(request):
    session = stripe.checkout.Session.create(
        mode="subscription",
        customer=request.user.profile.stripe_customer_id or None,
        payment_method_types=["card"],
        line_items=[{
            "price": settings.STRIPE_PRICE_ID,
            "quantity": 1,
        }],
        success_url=request.build_absolute_uri("/subscription/success/"),
        cancel_url=request.build_absolute_uri("/subscription/cancel/"),
    )

    if not request.user.profile.stripe_customer_id:
        request.user.profile.stripe_customer_id = session.customer
        request.user.profile.save()

    return redirect(session.url, code=303)


@login_required
def subscription_success(request):
    return render(request, "users/subscription_success.html")


@login_required
def subscription_cancel(request):
    return render(request, "users/subscription_cancel.html")


@login_required
def customer_portal(request):
    profile = request.user.profile

    # 顧客IDが無い＝未課金
    if not profile.stripe_customer_id:
        return redirect("/")

    session = stripe.billing_portal.Session.create(
        customer=profile.stripe_customer_id,
        return_url=request.build_absolute_uri("/"),
    )

    return redirect(session.url)