from django.contrib import admin
from .models import ArticleConversionLog


@admin.register(ArticleConversionLog)
class ArticleConversionLogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "post",
        "cta_type",
        "user",
        "created_at",
    )

    list_filter = (
        "cta_type",
        "created_at",
    )

    search_fields = (
        "post__title",
        "user__username",
    )

    ordering = ("-created_at",)
