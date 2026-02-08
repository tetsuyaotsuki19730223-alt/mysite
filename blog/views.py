from django.shortcuts import render, get_object_or_404
from .models import Post


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, is_published=True)

    # 無料記事
    if not post.is_premium:
        return render(request, "blog/post_detail.html", {
            "post": post,
            "can_view_premium": True,
        })

    # 未ログイン
    if not request.user.is_authenticated:
        return render(request, "blog/post_detail.html", {
            "post": post,
            "can_view_premium": False,
            "reason": "login_required",
        })

    # 課金チェック（★ここが本物）
    if not request.user.has_active_subscription():
        return render(request, "blog/post_detail.html", {
            "post": post,
            "can_view_premium": False,
            "reason": "subscription_required",
        })

    # 課金OK
    return render(request, "blog/post_detail.html", {
        "post": post,
        "can_view_premium": True,
    })
