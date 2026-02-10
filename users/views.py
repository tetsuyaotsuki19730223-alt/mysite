from django.http import HttpResponse
from django.conf import settings
import traceback

def subscribe(request):
    try:
        return HttpResponse(
            "\n".join([
                "SUBSCRIBE VIEW OK",
                f"STRIPE_SECRET_SET={bool(settings.STRIPE_SECRET_KEY)}",
                f"STRIPE_PRICE_ID={repr(settings.STRIPE_PRICE_ID)}",
                f"STRIPE_ENABLED={settings.STRIPE_ENABLED}",
            ]),
            content_type="text/plain"
        )
    except Exception:
        return HttpResponse(traceback.format_exc(), status=500)


def stripe_webhook(request):
    try:
        return HttpResponse("WEBHOOK OK", content_type="text/plain")
    except Exception:
        return HttpResponse(traceback.format_exc(), status=500)
