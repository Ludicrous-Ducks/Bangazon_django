from django.conf.urls import url
import sys
sys.path.append('../')
from bangazon_ui.views import register_view
from bangazon_ui.views import login_view
from bangazon_ui.views import product_view
from bangazon_ui.views import product_type_view

app_name = 'bangazon_ui'
urlpatterns = [


url(r'^register/$', register_view.Register.as_view(), name='register'),
url(r'^login/$', login_view.Login.as_view(), name='login'),
url(r'^logout/$', login_view.logout_user, name="logout"),
url(r'^product/$',product_view.Create_product.as_view(), name='product' ),
url(r'^product_type/$', product_type_view.Create_product_type.as_view(), name='product_type'),
url(r'^product_type_list/$', product_type_view.product_type, name='product_type_list'),


]