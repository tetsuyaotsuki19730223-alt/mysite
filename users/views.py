from django.http import HttpResponse
from django.conf import settings

def subscribe(request):
    return HttpResponse(
        f"""
        SUBSCRIBE VIEW OK
        STRIPE_SECRET_SET={bool(settings.STRIPE_SECRET_KEY)}
        STRIPE_PRICE_ID='{settings.STRIPE_PRICE_ID}'
        STRIPE_ENABLED={settings.STRIPE_ENABLED}
        """
    )

def stripe_webhook(request):
    return HttpResponse("ok")
