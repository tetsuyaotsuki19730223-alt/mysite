from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def subscription_required(view_func):
    @login_required
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = request.user

        # Profile が無い場合は未課金扱い
        profile = getattr(user, "profile", None)
        if not profile or not profile.is_subscribed:
            return redirect("/subscribe/")

        return view_func(request, *args, **kwargs)

    return _wrapped_view
