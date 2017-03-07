from django.contrib import admin
from django.contrib.auth.models import User
from Bangazon_api.models.customer_model import Customer
from Bangazon_api.models.payment_type_model import PaymentType
from Bangazon_api.models.product_model import Product
from Bangazon_api.models.product_type_model import ProductType
from Bangazon_api.models.order_model import Order


admin.site.register(Customer)
admin.site.register(PaymentType)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Order)