from django.shortcuts import redirect

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

        customer_id = session.get("customer")
        subscription_id = session.get("subscription")
        price_id = (
            session["items"]["data"][0]["price"]["id"]
            if "items" in session else settings.STRIPE_PRICE_ID
        )

        # ⚠️ 今はテストなので「最初のユーザー」を更新
        profile = Profile.objects.first()
        profile.is_subscribed = True
        profile.current_price_id = price_id
        profile.save()

        print("✅ Subscription activated")

    return HttpResponse("ok")

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
    )

    # ❌ return HttpResponse(...)
    # ✅ これだけ
    return redirect(session.url)
