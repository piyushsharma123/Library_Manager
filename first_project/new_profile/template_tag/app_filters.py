from django import template
register = template.Library()


@register.filter(name='abs')
def abs(value):
    return abs(value)