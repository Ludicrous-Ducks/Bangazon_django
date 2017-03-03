from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bangazon_ui.models import order_model
from bangazon_ui.models import payment_type_model
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from bangazon_ui.models import customer_model
from django.db.models import F, Sum, FloatField

class OrderDetail(TemplateView):
  """
    Thid method is to list order_detail in the Order Detail page
    Author Julia Kim-Chung
  """

  # order_list = Orders.objects.order_by('product_id')
  # product_list = Product.objects.order_by('product_id')
  template_name = 'bangazon_ui/order_detail_view.html'

  def get_context_data(self, **kwargs):
    customer = customer_model.Customer.objects.get(user = self.request.user.pk)
    order_list = order_model.Order.objects.get_or_create(customer=customer, completed = 0)
    payment_type_list = payment_type_model.PaymentType.objects.filter(customer=customer.pk)
    product_list = order_list[0].product.all()
    grand_total=product_list.aggregate(total=Sum(F('price'), output_field=FloatField()) )

    context = {'order_list': order_list[0], 'product_list': product_list, 'payment_type': payment_type_list }
    context.update(grand_total)
    return context

  def post(self, request):
      data = request.POST
      print(data)
      if data['payment'] == None:
          current_order = order_model.Order.objects.get(customer__user=request.user, completed = 0)
      else:
          return HttpResponseRedirect(redirect_to='/create_payment_type')

      if data['payment'] is not None:
          current_order = order_model.Order.objects.get(customer__user=request.user, completed = 0)
          current_order.completed=1
          current_order.save()
      else:
          return HttpResponseRedirect(redirect_to='/product_type_list')


