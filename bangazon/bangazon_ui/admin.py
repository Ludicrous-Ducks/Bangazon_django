from django.contrib import admin
from django.contrib.auth.models import User
from bangazon_ui.models.customer_model import Customer

admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Customer)