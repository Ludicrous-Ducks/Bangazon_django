from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bangazon_ui.models.customer_model import Customer


class Register(TemplateView):
    """
    """
    template_name = 'tutorial_app/register.html'


    def post(self, request):
        """
         
        """
        data = request.POST
        current_user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            password=data['password']
        )

        Customer.objects.create(
            user = current_user,
            address=data['address'],
            city=data['city'],
            state=data['state'],
            zip_code=data['zip_code'],
            phone=data['phone']
        )
        return HttpResponseRedirect(redirect_to='/login')
        return HttpResponse()
