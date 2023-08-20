from django import template
from app.models import Category, Comments

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_comments(post_id):
    return Comments.objects.filter(post_id=post_id).order_by('-time_create')
