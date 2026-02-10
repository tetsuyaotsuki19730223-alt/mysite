from django.http import HttpResponse
from django.conf import settings
import traceback

def subscribe(request):
    try:
        return HttpResponse(
            f"""
            STRIPE_ENABLED={settings.STRIPE_ENABLED}
            PRICE_ID={settings.STRIPE_PRICE_ID}
            SECRET_SET={bool(settings.STRIPE_SECRET_KEY)}
            """,
            content_type="text/plain"
        )
    except Exception as e:
        return HttpResponse(
            traceback.format_exc(),
            status=500,
            content_type="text/plain"
        )
