from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(
        "タイトル",
        max_length=200
    )

    free_content = models.TextField(
        "無料公開部分",
        blank=True,
        null=True,
        help_text="誰でも読める導入文"
    )

    premium_content = models.TextField(
        "有料コンテンツ",
        blank=True,
        null=True,
        help_text="サブスクユーザーのみ閲覧可能"
    )

    is_premium = models.BooleanField(
        "有料記事",
        default=False
    )

    is_published = models.BooleanField(
        "公開状態",
        default=True
    )

    published_at = models.DateTimeField(
        "公開日",
        default=timezone.now
    )

    created_at = models.DateTimeField(
        "作成日時",
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        "更新日時",
        auto_now=True
    )

    class Meta:
        ordering = ["-published_at"]
        verbose_name = "記事"
        verbose_name_plural = "記事"

    def __str__(self):
        return self.title
