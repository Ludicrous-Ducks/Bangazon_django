from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bangazon_ui.models import *
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth import views

  def post(self, request):
      data = request.POST
      if data['payment'] == None:
          current_order = order_model.Order.objects.get(customer__user=request.user, completed = 0)
          return HttpResponseRedirect(redirect_to='/payment_type_create')
      else:
          current_order = order_model.Order.objects.get(customer__user=request.user, completed = 0)
          current_order.completed=1
          current_order.save()
      return HttpResponseRedirect(redirect_to='/product_type_list')


