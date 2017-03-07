import sys
sys.path.append("../")
from django.db import models
from django.contrib.auth.models import User
from bangazon_ui.models.customer_model import Customer


class PaymentType(models.Model):
    """
    The PaymentType class represents a payment type tied to a particular User(Customer)
    of the Bangazon API.

    Variables:
    Foreign Key to the Customer Model
    payment_type
    account_number
    ccv
    expiration_date

    Author: Dani Adkins
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=100)
    account_number = models.CharField(max_length=16, unique=True)
    ccv = models.CharField(max_length=3)
    expiration_date = models.CharField(max_length=10)

    class Meta:
        """
        The Meta class creates a string representation of the plural instance of PaymentType

        Author: Dani Adkins
        """
        verbose_name_plural = 'PaymentTypes'

    def __str__(self):
        """
        A method to create a string representation of the payment type and account number
        on the Bagazon API

        Author: Dani Adkins
        """
        return '{} {}'.format(self.payment_type, self.account_number)