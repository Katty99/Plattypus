from django import template

register = template.Library()


@register.filter(name="balance_filter")
def price_filter(balance):
    return "%.2f" % balance
