from django.test import TestCase
import sys
sys.path.append('../')
from bangazon_ui.models.product_model import Product
from bangazon_ui.models.product_type_model import ProductType
from django.contrib.auth.models import User


class ProductTestCase(TestCase):
  """
   A class to test the Product model
   Author : Julia Kim-Chung
  """
  def setUp(self):
    Product.objects.create(
      name="lego", 
      price=100, 
      description="ultimate lego set", 
      quantity=2, 
      customer_id=0, 
      product_type_id=0)
    Product.objects.create(
      name="jigsaw puzzle", 
      price=30, 
      description="1000 piece puzzle", 
      quantity=3, 
      customer_id=1, 
      product_type_id=1)

  def test_product_has_lego(self):
    """
      a test method to check the product model field
    """
    lego = Product.objects.get(name='lego')
    self.assertEqual(lego.price, 100)
    self.assertEqual(lego.description, 'ultimate lego set')

  def test_product_has_jigsaw_puzzle(self):
    jigsaw_puzzle = Product.objects.get(name='jigsaw puzzle')
    self.assertEqual(jigsaw_puzzle.price, 30)
    self.assertEqual(jigsaw_puzzle.quantity, 3)



