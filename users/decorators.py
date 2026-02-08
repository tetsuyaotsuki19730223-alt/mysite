# users/decorators.py
from functools import wraps
from django.shortcuts import redirect, render

def subscription_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):

        # 未ログイン
        if not request.user.is_authenticated:
            return redirect("/accounts/login/")

        # プロフィール未作成ガード
        if not hasattr(request.user, "profile"):
            return redirect("/payments/subscribe/")

        # 未課金
        if not request.user.profile.is_subscribed:
            return redirect("/payments/subscribe/")

        return view_func(request, *args, **kwargs)

    return _wrapped_view
