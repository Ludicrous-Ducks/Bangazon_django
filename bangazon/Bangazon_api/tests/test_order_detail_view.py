from django.test import TestCase
import sys
sys.path.append('../')
from Bangazon_api.models.customer_model import Customer
from Bangazon_api.models.payment_type_model import PaymentType
from Bangazon_api.models.product_model import Product
from Bangazon_api.models.product_type_model import ProductType
from Bangazon_api.models.order_model import Order
from django.contrib.auth.models import User
from django.urls import reverse


class TestOrderDetailView(TestCase):
    """
    A class to test the Order Detail View
    """
    def setUp(self):
        self.user = User.objects.create_user(
            first_name="Suzi",
            last_name="Suzi",
            username="suzibee",
            password="suzi1234"
            )

        self.customer = Customer.objects.create(
            user=self.user,
            address="3040 NSS Drive",
            city="Nashville",
            state="TN",
            zip_code="12345",
            phone="123456789"
            )

        self.payment = PaymentType.objects.create(
            customer=self.customer,
            payment_type="Visa",
            account_number="12345678",
            ccv="111",
            expiration_date="2017-01-01"
            )
        self.product = Product.objects.create(
            name="lego", 
            price=100, 
            description="ultimate lego set", 
            quantity=2, 
            customer= self.customer, 
            )
        self.order= Order(
            completed=0, 
            customer = self.customer,
            payment_type = self.payment,
            )

        self.order.save()
        self.order.product.add(self.product)
        self.client.login(username='suzibee' , password='suzi1234')

    def test_order_detail_view_shows_correct_order(self):
        """
            a test method to check the order model field
        # """
        response = self.client.get(reverse('Bangazon_api:order_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertIn( "{'order_list': <Order: 0>, 'product_list': <QuerySet [<Product: lego>]>, 'payment_type': <QuerySet [<PaymentType: Visa 12345678>]>}", str(response.context))

        





        

        
        