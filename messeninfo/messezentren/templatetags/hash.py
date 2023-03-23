
from django import template
register = template.Library()


@register.filter
def hash(h, key):
    return h[key]


@register.simple_tag
def concat(val=None, val2=None):
    return val + "_" + val2
