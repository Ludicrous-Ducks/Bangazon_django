from django.test import TestCase
import sys
sys.path.append('../')
from django.contrib.auth.models import User
from Bangazon_api.models.customer_model import Customer
from Bangazon_api.models.payment_type_model import PaymentType
from Bangazon_api.models.product_type_model import ProductType
from Bangazon_api.models.product_model import Product
from Bangazon_api.models.order_model import Order
from Bangazon_api.views.add_to_order_view import *
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

        response = self.client.post(reverse('Bangazon_api:add_to_order'), to_add)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'You Added a Product!')
