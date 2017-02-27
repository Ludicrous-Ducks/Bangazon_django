from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bangazon_ui.models.customer_model import Customer
from bangazon_ui.models.order_model import Order
from bangazon_ui.models.product_model import Product

def add_to_order(request):
    """
    
    """
    request_data = request.POST
    current_user = request.user
    current_customer = Customer.objects.get(user=current_user.pk)
    myorder = Order.objects.get(customer=current_customer.pk, completed=0)
    product = Product.objects.get(pk=request_data['product_pk'])
    myorder.product.add(product)
    myorder.save()

    return HttpResponse('You Added a Product!')
