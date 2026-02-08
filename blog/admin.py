from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "is_premium", "is_published", "published_at")
    list_filter = ("is_premium", "is_published")
    search_fields = ("title", "free_content")