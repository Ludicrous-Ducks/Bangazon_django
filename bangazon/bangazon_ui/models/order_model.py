import sys
sys.path.append("../")
from django.db import models
from django.contrib.auth.models import User
from bangazon_ui.models.customer_model import Customer
from bangazon_ui.models.payment_type_model import PaymentType
from bangazon_ui.models.product_model import Product



class Order (models.Model):
    """
    The Order table pulls information from PaymentType and Product via a join 
    """

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.IntegerField(default = 0)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)

    class Meta:
        verbose_name_plural = "Orders"

    def __str__(self):
        return '{} {}'.format(self.active, self.customer.first_name)