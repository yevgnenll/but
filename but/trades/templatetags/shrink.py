from django import template


register = template.Library()


@register.filter
def shrink(value):
    from but.utils import shrink_content
    return shrink_content(value)
