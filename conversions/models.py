from django.conf import settings
from django.db import models
from blog.models import Post


class ArticleConversionLog(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="conversion_logs"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    cta_type = models.CharField(
        max_length=30,
        default="subscribe"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.title} / {self.cta_type}"
