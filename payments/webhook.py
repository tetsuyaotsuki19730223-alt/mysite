print(json.dumps(data, indent=2))
import stripe

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

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]

        user_id = session.get("client_reference_id")
        customer_id = session.get("customer")
        subscription_id = session.get("subscription")

        profile = Profile.objects.get(user_id=user_id)
        profile.is_subscribed = True
        profile.stripe_customer_id = customer_id
        profile.stripe_subscription_id = subscription_id
        profile.save()

        print("✅ subscription activated for user:", user_id)

    return HttpResponse(status=200)
