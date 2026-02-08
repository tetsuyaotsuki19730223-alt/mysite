from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from users.models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "プロフィール"
    fk_name = "user"


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

    list_display = (
        "username",
        "email",
        "is_staff",
        "is_active",
        "is_superuser",
    )

    fieldsets = (
        (None, {
            "fields": ("username", "password")
        }),
        ("個人情報", {
            "fields": ("first_name", "last_name", "email")
        }),
        ("権限", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("重要な日時", {
            "fields": ("last_login", "date_joined")
        }),
    )
