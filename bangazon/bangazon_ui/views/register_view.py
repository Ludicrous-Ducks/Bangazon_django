from django.views.generic.base import TemplateView
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from bangazon_ui.models.customer_model import Customer
from django.http import HttpResponseRedirect


class Register(TemplateView):
    """
    A Class, based on TemplateView Class for registering a new user of the Bangazon site. Consists of a template name and one over-loaded method.

    Methods:
        post: Method to post data to two models: Django's built-in User Model and the Bangazon "Customer" model, based on form data from the template

            Arguments: request data

            Request data consists of
                username
                email
                first_name
                last_name
                password
                user
                address
                city
                state
                zip_code
                phone

    Author: Ben Marks, Ludicrous Ducks
    """

    template_name = 'bangazon_ui/registration.html'


    def post(self, request):
        """
        Override method for the default post method. Posts data into two models: Django default "User" model and a custom Bangazon "Customer" model which integrates a django User model.
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
