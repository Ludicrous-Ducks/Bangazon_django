from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bangazon_ui.models.product_model import Product
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate

class ProductDetailView(DetailView):
    """
    Class to define the product detail view
    Template includes a button for adding the product to cart
        template = product_detail_view.html

    Author: Ben Marks, Ludicrous Ducks
    """

    template_name = 'bangazon_ui/product_detail_view.html'
    model = Product
