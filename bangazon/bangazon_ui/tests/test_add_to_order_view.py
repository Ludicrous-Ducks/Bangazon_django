from django.test import TestCase
import sys
sys.path.append('../')
from django.contrib.auth.models import User
from bangazon_ui.models.customer_model import Customer
# from bangazon_ui.models.order_model import Order
from bangazon_ui.views.add_to_order_view import AddToOrderView
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
        
        response = self.client.post(reverse('bangazon_ui:add_to_order'), customer)
        self.assertEqual(response.content, 'You Added a Product!')
        self.assertEqual(response.url, "/login")