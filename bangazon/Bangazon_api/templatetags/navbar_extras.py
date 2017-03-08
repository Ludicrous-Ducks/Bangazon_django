from Bangazon_api.models.customer_model import Customer
from Bangazon_api.models.order_model import Order
from Bangazon_api.models.product_model import Product
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def welcome(context):
    """
    Method to create a custom welcome tag based on the current user context

    Arguments: None
    Returns: A string including the user's full name

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

    Arguments: None
    Returns: Then integer length of the products found on a user's current order

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
