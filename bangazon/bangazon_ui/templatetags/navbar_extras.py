from bangazon_ui.models.customer_model import Customer
from bangazon_ui.models.order_model import Order
from bangazon_ui.models.product_model import Product
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def welcome(context):
    """
    Method to create a custom welcome tag based on the current user context

    Author: Ben Marks, Ludicrous Ducks
    """
    user = context['user']
    if user.is_authenticated():
        customer = Customer.objects.get(user = user.pk)
        message = "Welcome, {} {}".format(customer.user.first_name, customer.user.last_name)
    else:
        message = ""

    return message

@register.simple_tag(takes_context=True)
def cart(context):
    """
    Method to create a custom cart total tag based on the current user context

    Author: Ben Marks, Ludicrous Ducks
    """
    user = context['user']
    if user.is_authenticated():
        customer = Customer.objects.get(user = user.pk)
        try:
            order = Order.objects.get_or_create(customer=customer, completed = 0)
            product_list = order[0].product.all()
        except:
            product_list = []
    else:
        product_list = []

    product_count = len(product_list)
    return product_count

@register.simple_tag(takes_context=True)
def log_button(context):
    """
    Method to return the correct button dependin on user status
    """
    user = context['user']
    if user.is_authenticated():
        button = "logout"
    else:
        button = "login"

    return button