from django.test import TestCase
from bangazon_ui.models.product_model import Product
from bangazon_ui.models.product_type_model import ProductType
from django.contrib.auth.models import User


class ProductTypeTestCase(TestCase):
	def setUp(self):
		ProductType.objects.create(label ="electronics")

	def test_product_type_has_electronics(self):
		electronics = ProductType.objects.get(label='electronics')
		self.assertEqual(electronics.label, "electronics")

