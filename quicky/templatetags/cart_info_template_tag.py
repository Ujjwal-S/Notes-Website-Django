from django import template
from django.template import context
from quicky.models import Order, User, OrderItem

register = template.Library()


@register.simple_tag(takes_context=True)
def total_items_in_cart(context):
    try:
        order = Order.objects.get(customer=context['user'], complete=False)
        return OrderItem.objects.filter(order=order).count()
    except:
        return 0
