from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bangazon_ui.models import *
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate


def home(request):
    product_list = Product.objects.order_by('created')[:20]
    context = {'product_list': product_list,}
    return render(request, 'bangazon_ui/product_list.html', context)

def create_product(request):
    data = request.POST
    product_type = ProductType.objects.get_or_create(label=data['label'])
    Product.objects.create(
        name=data['name'],
        price=data['price'],
        description=data['description'],
        quantity=data['quantity'],
        product_type =product_type[0],
        customer=request.user)
    return HttpResponseRedirect(redirect_to='/list')

def template_to_create(request):
    return render(request, 'bangazon_ui/create_product.html')