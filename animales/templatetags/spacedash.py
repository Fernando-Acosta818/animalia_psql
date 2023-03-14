from django import template

register = template.Library()

@register.filter(name='rep')
def rep(str):
    return str.replace(" ", "-")
