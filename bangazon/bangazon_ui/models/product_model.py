from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Product(models.Model):
    """
    Class to represent a product for sale on Bangazon
    tied to a
    particular User(customer) of bangazon API
    Extension of models.Model
    Variables:
        created: the current local date and time of creation
        name: the product's name
        
        customer: the foreign key of the user, related_name is for the PaymentMethod model: related_name should be lowercase, pluralized model name
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default="")
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField(max_length=300, default='')
    quantity = models.IntegerField()
    product_type =models.ForeignKey("ProductType", related_name="products", on_delete=models.CASCADE)
    customer =models.ForeignKey(User, related_name="products", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        """
        Method to create a string representing a Product sold/bought by a particular User(customer)
     
        """

    class Meta:
        ordering =('name', )

