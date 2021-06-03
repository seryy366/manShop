from django import template
from shop.models import Post

register = template.Library()


@register.inclusion_tag('shop/popular_posts_tpl.html')
def get_popular(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {"posts": posts}
