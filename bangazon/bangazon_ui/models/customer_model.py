import sys
sys.path.append("../")
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """
    The Customer table integrates the Django User model and maintains relevant information for
    a Bangazon User(Customer)

    Variables:
    One to One Field to the Django User model
    address
    city
    state
    zip_code
    phone

    Author: Dani Adkins
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    class Meta:
        """
        The Meta class creates a string representation of the plural instance of Customer
        """
        verbose_name_plural = "Customers"

    def __str__(self):
        """
        A method to create a string representation of the Bangazon User(Customer)'s username
        on the Bagazon API
        """
        return '{}'.format(self.user.username)




