from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Bangazon_api.models import *
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth import views

 def post(self, request):
      """
      The post method will allow the current Customer(User) to close the order after a product
      and payment type have been added. The user will not be able to close an order before
      entering a payment type.

      Author: Dani Adkins
      """
      data = request.POST
      try:
          current_order = order_model.Order.objects.get(customer__user=request.user, completed = 0)
          current_order.payment_type = payment_type_model.PaymentType.objects.get(pk=data['payment'])
          current_order.completed=1
          current_order.save()
          return HttpResponseRedirect(redirect_to='/product_type_list')
      except MultiValueDictKeyError:
          return HttpResponseRedirect(redirect_to='/payment_type_create')


