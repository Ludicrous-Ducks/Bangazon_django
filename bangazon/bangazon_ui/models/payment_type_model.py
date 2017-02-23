import sys
sys.path.append("../")
from django.db import models
from django.contrib.auth.models import User
from bangazon_ui.models.customer_model import Customer


class PaymentType(models.Model):
    """
    The PaymentType table maintains the different payment options associated with a customer
    Author: Dani Adkins
    """

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=100)
    account_number = models.CharField(max_length=16, unique=True)
    ccv = models.CharField(max_length=3)
    expiration_date = models.DateField()

    class Meta:
        verbose_name_plural = 'PaymentTypes'

    def __str__(self):
        return '{} {}'.format(self.payment_type, self.account_number)