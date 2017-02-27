from django.test import TestCase
import sys
sys.path.append('../')
from django.contrib.auth.models import User
from bangazon_ui.models.customer_model import Customer
from bangazon_ui.models.payment_type_model import PaymentType
from bangazon_ui.models.product_type_model import ProductType
from bangazon_ui.models.product_model import Product
from bangazon_ui.models.order_model import Order
from bangazon_ui.views.add_to_order_view import *
from django.urls import reverse


class TestAddToOrder(TestCase):
    """
    A class to test the Add to Order functions correctly
    """

    def test_add_to_order_should_post_correctly(self):
        """
        """

        user = User.objects.create_user(
            first_name="Dani",
            last_name="Dani",
            username="danidani",
            password="asdf1234"
        )

        customer = Customer.objects.create(
            user=user,
            address="3040 NSS Drive",
            city="Nashville",
            state="TN",
            zip_code="12345",
            phone="123456789"
        )

        payment = PaymentType.objects.create(
            customer=customer,
            payment_type="Visa",
            account_number="12345678",
            ccv="111",
            expiration_date="2017-01-01"
        )

        product_type = ProductType.objects.create(
            label= 'musical instruments'
        )

        product = Product.objects.create(
            customer = customer,
            name = 'cello',
            price = '100',
            description = 'yoyo-ma',
            product_type = product_type,
            quantity = 5
        )

        order = Order.objects.create(
            customer=customer,
            payment_type= payment,
        )

        to_add = {'product_pk': 1}

        self.client.force_login(user)

        response = self.client.post(reverse('bangazon_ui:add_to_order'), to_add)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'You Added a Product!')
