from django.contrib import admin
from django.contrib.auth.models import User
from bangazon_ui.models.customer_model import Customer
from bangazon_ui.models.payment_type_model import PaymentType
from bangazon_ui.models.product_model import Product
from bangazon_ui.models.product_type_model import ProductType



admin.site.register(Customer)
admin.site.register(PaymentType)
admin.site.register(ProductType)
admin.site.register(Product)