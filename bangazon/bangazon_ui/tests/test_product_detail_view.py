import sys
sys.path.append("../")
from django.test import TestCase
from bangazon_ui.models.payment_type_model import PaymentType
from bangazon_ui.models.product_model import Product
from django.contrib.auth.models import User


class TestPaymentType(TestCase):
    """
    This is the test class for the Product Detail View
    Author: Ben Marks, Ludicrous Ducks
    """
