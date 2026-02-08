from django.db.models import Count, Q
from blog.models import Post
from conversions.models import ArticleConversionLog


def weak_articles():
    return (
        Post.objects
        .annotate(
            views=Count(
                "articleconversionlog",
                filter=Q(articleconversionlog__cta_type__isnull=False),
                distinct=True
            ),
            conversions=Count(
                "articleconversionlog",
                filter=Q(articleconversionlog__cta_type="purchase"),
                distinct=True
            ),
        )
        .filter(views__gte=50)
        .annotate(
            cv_rate=models.ExpressionWrapper(
                models.F("conversions") * 1.0 / models.F("views"),
                output_field=models.FloatField()
            )
        )
        .filter(cv_rate__lt=0.02)
        .order_by("cv_rate")
    )
