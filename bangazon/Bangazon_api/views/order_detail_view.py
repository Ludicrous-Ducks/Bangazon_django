from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Bangazon_api.models import order_model
from Bangazon_api.models import product_model
from Bangazon_api.models import payment_type_model
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from Bangazon_api.models import customer_model
from django.db.models import F, Sum, Count, FloatField

class OrderDetail(TemplateView):
  """
    Thid method is to list order_detail in the Order Detail page
    Author Julia Kim-Chung
  """
  template_name = 'Bangazon_api/order_detail_view.html'

  def get_context_data(self, **kwargs):
    customer = customer_model.Customer.objects.get(user = self.request.user.pk)
    order_list = order_model.Order.objects.get_or_create(customer=customer, completed = 0)
    payment_type_list = payment_type_model.PaymentType.objects.filter(customer=customer.pk)
    product_list = order_list[0].product.all().annotate(Count('id')).order_by('id')
    grand_total=order_list[0].product.aggregate(total=Sum('price', output_field=FloatField()) )

    context = {'order_list': order_list[0], 'product_list': product_list, 'payment_type': payment_type_list }
    context.update(grand_total)
    return context


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

