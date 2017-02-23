from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from bangazon_ui.models import *
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate


class Login(TemplateView):
    template_name = 'bangazon_ui/login.html'

    def post(self, request):

        data=request.POST
        username=data['username']
        password=data['password']
        user=authenticate(
            username=username,
            password=password)
        if user is not None:
            login(request=request, user=user)
        else:
            return HttpResponseRedirect(redirect_to='/')
        return HttpResponseRedirect(redirect_to='/')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(redirect_to='/')