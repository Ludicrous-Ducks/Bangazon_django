from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bangazon_ui.models import order_model
from bangazon_ui.models import payment_type_model
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from bangazon_ui.models import customer_model
from django.db.models import F, Sum, FloatField
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
        customer = customer_model.Customer.objects.get(user = self.request.user.pk)
        try:
            order = order_model.Order.objects.get_or_create(customer=customer, completed = 0)
            product_list = order[0].product.all()
        except:
            product_list = []
        product_count = len(product_list)
        message = "Welcome, {} {}".format(customer.user.first_name, customer.user.last_name)
    else:
        message = ""
        product_list = []

    return { 'message': message, 'product_count': product_count }

