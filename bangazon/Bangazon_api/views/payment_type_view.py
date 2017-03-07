from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Bangazon_api.models import *
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth import views
from Bangazon_api.models.customer_model import Customer
from Bangazon_api.models.payment_type_model import PaymentType


class PaymentTypeView(TemplateView):
    """
    The PaymentTypeView will display the payment type information to the DOM for viewing by the current customer/user
    Author: Dani Adkins
    """
    template_name = 'Bangazon_api/create_payment_type.html'

    def post(self, request):
        """
        The post method will allow the user to add payment credentials
        Once payment credentials have been entered it will then re-route to the order page
        Author: Dani Adkins
        """

        data = request.POST
        current_customer = Customer.objects.get(user=request.user)
        add_payment = PaymentType.objects.create(
            customer=current_customer,
            payment_type=data['payment_type'],
            account_number=data['account_number'],
            ccv=data['ccv'],
            expiration_date=data['expiration_date']
            )
        return HttpResponseRedirect(redirect_to='/order_detail')