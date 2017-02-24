from django.conf.urls import url
import sys
sys.path.append('../')
from bangazon_ui.views import register_view
from bangazon_ui.views import login_view
from bangazon_ui.views import payment_type_view
from bangazon_ui.views import product_view
from bangazon_ui.views import product_type_view

app_name = 'bangazon_ui'
urlpatterns = [
url(r'^$', register_view.Register.as_view(), name='register'),
url(r'^register/$', register_view.Register.as_view(), name='register'),
url(r'^login/$', login_view.Login.as_view(), name='login'),
url(r'^logout/$', login_view.logout_user, name="logout"),
url(r'^payment_type_create/$', payment_type_view.PaymentTypeView.as_view(), name="payment_type_create"),
url(r'^product/$',product_view.create_product, name='product' ),
url(r'^create/$', product_view.template_to_create, name='create'),
url(r'^product_type/$', product_type_view.create_product_type, name='product_type'),
url(r'^create_product_type/$', product_type_view.template_to_create_product_type, name='create_product_type'),
url(r'^product/$',product_view.Create_product.as_view(), name='product' ),
url(r'^product_type/$', product_type_view.Create_product_type.as_view(), name='product_type'),
url(r'^product_type_list/$', product_type_view.product_type, name='product_type_list'),
]