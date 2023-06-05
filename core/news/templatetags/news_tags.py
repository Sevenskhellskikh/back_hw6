from django import template
from django.db.models import Count

from news.models import Category


register = template.Library()


@register.simple_tag()
def get_categories():
    categories = Category.objects.annotate(count=Count('news')).filter(count__gt=0)
    return categories
