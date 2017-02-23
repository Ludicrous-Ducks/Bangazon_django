from django.test import TestCase
import sys
sys.path.append('../')
from bangazon_ui.models.product_model import Product
from bangazon_ui.models.product_type_model import ProductType
from django.contrib.auth.models import User


class ProductTypeTestCase(TestCase):
	"""
	 	A class to test ProductType model
	"""
	def setUp(self):
		ProductType.objects.create(label ="electronics")

	def test_product_type_has_electronics(self):
		"""
			a test method to check the product type field
		"""
		electronics = ProductType.objects.get(label='electronics')
		self.assertEqual(electronics.label, "electronics")

