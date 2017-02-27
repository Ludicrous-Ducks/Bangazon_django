from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bangazon_ui.models import *
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth import views

class CloseOrderView(TemplateView):

    template_name = 'bangazon_ui/order_detail_view.html'

    def post(self, request):
        data = request.post
        current_order = Order.objects.get(customer__user=request.user)
        current_order.completed=1
        current_order.save()

        return HttpResponseRedirect(redirect_to='/product_type_list')



