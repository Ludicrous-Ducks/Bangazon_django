import sys
sys.path.append("../")
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ProductType(models.Model):

    """ 
    This class is to represent a category of products on Bangazon
    Extension of models.Model
    Variables:
        label: the Product type's name
    """
    label = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.label

    """
    Method to create a string representing a Product Category of
    Bangazon API
    """

    class Meta:

        ordering=('label',)
