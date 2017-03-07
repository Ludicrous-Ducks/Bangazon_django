import sys
sys.path.append("../")
from django.test import TestCase
from Bangazon_api.models.payment_type_model import PaymentType
from Bangazon_api.models.payment_type_model import Customer
from Bangazon_api.models.product_model import Product
from Bangazon_api.models.order_model import Order
from Bangazon_api.models.product_type_model import ProductType
from django.contrib.auth.models import User


class TestCloseOrderView(TestCase):
    """
    This is the test class for the CloseOrderView
    Author: Dani Adkins
    """

    def test_customer_can_close_order(self):
        """
        This test will test that the customer's order can be closed - completed will change from 0 to 1
        Author: Dani Adkins
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
            payment_type=payment,
            )

        order.product.add(product)
        order.save()

        self.assertIsInstance(order.customer, Customer)
        self.assertIsInstance(order.payment_type, PaymentType)

        order_test = {
            'customer' : customer,
            'payment_type': payment,
            'completed' : '1'
            }

        current_order = Order.objects.get(customer=customer)
        current_order.completed=1
        current_order.save()
        self.assertEqual(current_order.completed, 1)
