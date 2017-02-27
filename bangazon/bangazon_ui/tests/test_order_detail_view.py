from django.test import TestCase
import sys
sys.path.append('../')
from bangazon_ui.models.customer_model import Customer
from bangazon_ui.models.payment_type_model import PaymentType
from bangazon_ui.models.product_model import Product
from bangazon_ui.models.product_type_model import ProductType
from bangazon_ui.models.order_model import Order
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import F, Count

# from bangazon_ui.models.orders_model import Orders

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


    def test_order_detail_view_shows_correct_order(self):
        """
            a test method to check the order model field
        # """
        response = self.client.get(reverse('bangazon_ui:order_detail',  args=[self.order.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertIn( "{'order_list': <Order: 0>, 'product_list': <QuerySet [<Product: lego>]>}", str(response.context))

        





        # queryset = self.order.objects.all().order_by('product_id').filter(product_id = self.product.pk)
        # queryset_p = self.product.objects.all()
        # products = self.product.annotate(Count(self.product.pk))
        # print(products)



        
        