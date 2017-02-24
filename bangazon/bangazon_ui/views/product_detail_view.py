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
    model = Product
    
    # def get(self, request, pk):
    #     """
    #     A method to return the desired populated template
    #     """
        
    #     return HttpResponse()
