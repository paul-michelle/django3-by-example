from typing import Dict
from django import template
from markdown import markdown
from django.utils.safestring import mark_safe
from django.db.models import QuerySet, Count
from ..models import Post

register = template.Library()
LATEST_POSTS_COUNT = 3
POPULAR_POSTS_COUNT = 3


@register.simple_tag(name='posts_total')
def get_published_posts_total() -> int:
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def get_latest_posts(count: int = LATEST_POSTS_COUNT) -> Dict[str, QuerySet]:
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_popular_posts(count: int = POPULAR_POSTS_COUNT) -> QuerySet:
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    formatted_text = markdown(text)
    return mark_safe(formatted_text)
