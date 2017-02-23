from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bangazon_ui.models import *
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate

class ProductDetailView(TemplateView):
    """
    Class to define the product detail view, including a button for adding the product to cart

    Author: Ben Marks, Ludicrous Ducks
    """

    template_name = 'bangazon_ui/product_detail_view'
    pass