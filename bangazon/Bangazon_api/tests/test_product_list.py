from django.test import TestCase
import sys
sys.path.append('../')
from Bangazon_api.models.product_model import Product
from Bangazon_api.models.product_type_model import ProductType
from Bangazon_api.models.customer_model import Customer
from django.contrib.auth.models import User
from Bangazon_api.views.product_list_view import ProductListView
from django.urls import reverse


class TestProductList(TestCase):
    """
    a class to test that only products of a certain type can be returned and listed
    """

    def setUp(self):
        self.user = User.objects.create_user(first_name='jack',
                                        last_name='pinky',
                                        username='greg',
                                        password='password')
        self.customer = Customer.objects.create(user=self.user,
                                        address='666 wishfull lane',
                                        city='lake fo fire',
                                        state='TN',
                                        zip_code='12345',
                                        phone='123456789')
        self.product_type1 = ProductType.objects.create(label = 'electronic')
        self.product_type2 = ProductType.objects.create(label = 'toy')
        self.product1 = Product.objects.create(customer=self.customer,
                                        name='dell computer',
                                        price=2.00,
                                        description='yeah',
                                        product_type=self.product_type1,
                                        quantity=100)
        self.product2 = Product.objects.create(customer=self.customer,
                                        name='thingy',
                                        price=2.00,
                                        description='yeah',
                                        product_type=self.product_type2,
                                        quantity=100)

    def test_canGetProductByType(self):
        """
        test that you can get products by type
        """
        response = self.client.get(reverse('Bangazon_api:product_list', args=([self.product_type1.pk])))
        self.assertIn("{'product_list': <QuerySet [<Product: dell computer>]>}", str(response.context))
