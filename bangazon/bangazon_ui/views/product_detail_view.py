from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bangazon_ui.models.product_model import Product
from bangazon_ui.models.customer_model import Customer
from bangazon_ui.models.product_type_model import ProductType
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate

class ProductDetailView(TemplateView):
    """
    Class to define the product detail view, including a button for adding the product to cart

    Author: Ben Marks, Ludicrous Ducks
    """

    template_name = 'bangazon_ui/product_detail_view'
    
    def get_details(product_pk):
        """
        """
        product = Product.objects.get(pk=product_pk)
        customer = Customer.objects.get(pk=product.customer.pk)
        product_type = ProductType.objects.get(pk=product.product_type.pk)
        product_details = {
            'name': product.name,
            'product_type': product.product_type.__str__(),
            'description': product.description,
            'quantity': str(product.quantity),
            'price': str(product.price),
            'customer': product.customer.user.username,
            'created': product.created.date().__str__()
        }
        return product_details