from django.contrib.auth.models import User
from django.db import models

class Customer(models.Model):
    """
    The customers table integrates the Django User model and maintains relevant information for a customer
    Author: Dani Adkins
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Customers"

    def __str__(self):
        return '{}'.format(self.user.username)



