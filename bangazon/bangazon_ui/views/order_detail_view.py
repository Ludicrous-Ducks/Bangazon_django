from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bangazon_ui.models import order_model
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate

class OrderDetail(TemplateView):
  """
    Thid method is to list order_detail in the Order Detail page
    Author Julia Kim-Chung
  """

  # order_list = Orders.objects.order_by('product_id')
  # product_list = Product.objects.order_by('product_id')
  template_name = 'bangazon_ui/order_detail_view.html'
  
  def get_context_data(self, **kwargs):

    order_list = order_model.Order.objects.get(pk =kwargs['order_id'])
    product_list = order_list.product.all()
    context = {'order_list': order_list, 'product_list': product_list}

    return context

    

  