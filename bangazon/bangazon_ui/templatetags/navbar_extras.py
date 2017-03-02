from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bangazon_ui.models.customer_model import Customer
from bangazon_ui.models.order_model import Order
from bangazon_ui.models.product_model import Product
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def welcome_and_cart(context):
    """
    Method to create a custom tag based on the current user context

    Author: Ben Marks, Ludicrous Ducks
    """

    user = context.user
    if user.is_authenticated():
        customer = Customer.objects.get(user = self.request.user.pk)
        try:
            order = Order.objects.get_or_create(customer=customer, completed = 0)
            product_list = order[0].product.all()
        except:
            product_list = []
        message = "Welcome, {} {}".format(customer.user.first_name, customer.user.last_name)
    else:
        message = ""
        product_list = []

    product_count = len(product_list)
    return { 'message': message, 'product_count': product_count }

