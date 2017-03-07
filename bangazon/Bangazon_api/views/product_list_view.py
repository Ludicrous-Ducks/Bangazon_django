from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Bangazon_api.models import *
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate


class ProductListView(TemplateView):

	template_name = 'Bangazon_api/product_list.html'
	
	def get_context_data(self, **kwargs):
		product_list = product_model.Product.objects.filter(product_type = kwargs['pk'])
		product_type = product_type_model.ProductType.objects.get(pk = kwargs['pk'])
		return {'product_list': product_list, 'product_type': product_type}


