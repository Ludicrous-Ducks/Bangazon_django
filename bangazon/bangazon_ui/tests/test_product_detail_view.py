import sys
sys.path.append("../")
from django.test import TestCase
from django.contrib.auth.models import User
from bangazon_ui.models.customer_model import Customer
from bangazon_ui.models.product_model import Product
from bangazon_ui.models.product_type_model import ProductType
from bangazon_ui.views.product_detail_view import ProductDetailView


class TestProductDetailView(TestCase):
    """
    This is the test class for the Product Detail View

    Author: Ben Marks, Ludicrous Ducks
    """

    def test_product_detail_view_should_return_product_details(self):
        """
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

        detail = ProductDetailView.get_details(product_pk=1)
        self.assertEqual(detail['name'], "lego")
        self.assertEqual(detail['product_type'], "Toys")
        self.assertEqual(detail['description'], "ultimate lego set")
        self.assertEqual(detail['quantity'], "2")
        self.assertEqual(detail['price'], "100.00")
        self.assertEqual(detail['customer'], "danidani")
