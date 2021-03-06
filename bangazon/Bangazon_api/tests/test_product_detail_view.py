import sys
sys.path.append("../")
from django.test import TestCase
from django.contrib.auth.models import User
from Bangazon_api.models.customer_model import Customer
from Bangazon_api.models.product_model import Product
from Bangazon_api.models.product_type_model import ProductType
from Bangazon_api.views.product_detail_view import ProductDetailView
from django.urls import reverse


class TestProductDetailView(TestCase):
    """
    This is the test class for the Product Detail View

    Author: Ben Marks, Ludicrous Ducks
    """

    def test_product_detail_view_should_return_product_details(self):
        """
        Method to ensure that the detail view is sending the correct product object to the template.
        """
        test_user = User.objects.create_user(
            first_name="Dani",
            last_name="Dani",
            username="danidani"
            )

        test_customer = Customer.objects.create(
            user=test_user,
            address="3040 NSS Drive",
            city="Nashville",
            state="TN",
            zip_code="12345",
            phone="123456789"
            )

        test_product_type = ProductType.objects.create(label="Toys")

        test_product = Product.objects.create(
            name="lego",
            price=100,
            description="ultimate lego set",
            quantity=2,
            customer=test_customer,
            product_type=test_product_type)

        response = self.client.get(reverse('Bangazon_api:product_detail', args=([test_product.pk])))
        self.assertEqual(response.context['product'].name, 'lego')
