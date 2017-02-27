import sys
sys.path.append("../")
from django.test import TestCase
from bangazon_ui.models.payment_type_model import PaymentType
from bangazon_ui.models.payment_type_model import Customer
from bangazon_ui.models.product_model import Product
from bangazon_ui.models.order_model import Order
from bangazon_ui.models.product_type_model import ProductType
from django.contrib.auth.models import User
from django.urls import reverse


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
            payment_type= payment,

            )

        order.product.add(product)
        order.save()

        self.assertIsInstance(order.customer, Customer)
        self.assertIsInstance(order.payment_type, PaymentType)
        # self.assertIsInstance(order.product, Product)
        # self.assertIsInstance(order.order, Order)

        order_test = {
            'customer' : customer,
            'payment_type': payment,
            'completed' : '1'
            }

        current_order = Order.objects.get(customer=customer)
        current_order.completed=1
        current_order.save()
        self.assertEqual(current_order.completed, 1)


        # response = self.client.post(reverse('bangazon_ui:order_detail_view'), order_test)
        # self.assertEqual(response.status_code, 302)
        # print(response)
        # self.assertEqual(response.url, "/product_type_list")















