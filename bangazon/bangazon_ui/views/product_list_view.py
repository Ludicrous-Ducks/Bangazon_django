from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bangazon_ui.models import *
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate


class ProductListView(TemplateView):

	template_name = 'bangazon_ui/product_list.html'
	# model = product_model.Product
	def get_context_data(self, **kwargs):
		product_list = product_model.Product.objects.filter(product_type = kwargs['pk'])
		return {'product_list': product_list}
