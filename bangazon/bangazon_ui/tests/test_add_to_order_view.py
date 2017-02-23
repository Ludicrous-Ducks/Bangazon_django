from django.test import TestCase
import sys
sys.path.append('../')
from django.contrib.auth.models import User
from bangazon_ui.models.customer_model import Customer
from bangazon_ui.models.order_model import Order
from bangazon_ui.views.add_to_order_view import AddToOrderView
from django.urls import reverse
