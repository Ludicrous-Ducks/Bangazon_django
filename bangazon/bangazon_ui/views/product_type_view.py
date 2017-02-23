from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bangazon_ui.models import *
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate


def product_type(request):
    product_type_list = ProductType.objects.order_by("label")[:20]
    context = {'product_type_list': product_type_list,}
    return render(request, 'bangazon_ui/product_type_list.html', context)


def create_product_type(request):
    data = request.POST
    ProductType.objects.create(
        label=data['label'])

    return HttpResponseRedirect(redirect_to='/product_type_list')


def template_to_create_product_type(request):
    return render(request, 'bangazon_ui/create_product_type.html')
