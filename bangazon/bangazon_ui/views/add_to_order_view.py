from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bangazon_ui.models.customer_model import Customer
from bangazon_ui.models.order_model import Order

def add_to_order(request):
    """
    
    """
    
    current_user = request(user)
    current_customer = Customer.objects.get(user=user.pk)
    myorder = Order.objects.get(customer=current_customer.pk)
