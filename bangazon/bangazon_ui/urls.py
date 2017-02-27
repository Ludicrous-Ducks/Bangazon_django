from django.conf.urls import url
import sys
sys.path.append('../')
from bangazon_ui.views import register_view
from bangazon_ui.views import login_view
from bangazon_ui.views import payment_type_view
from bangazon_ui.views import product_view
from bangazon_ui.views import product_type_view
from bangazon_ui.views.product_detail_view import ProductDetailView
from bangazon_ui.views.add_to_order_view import *
from bangazon_ui.views import order_detail_view

app_name = 'bangazon_ui'
urlpatterns = [
    url(r'^$', register_view.Register.as_view(), name='register'),
    url(r'^register/', register_view.Register.as_view(), name='register'),
    url(r'^login/', login_view.Login.as_view(), name='login'),
    url(r'^logout/', login_view.logout_user, name="logout"),
    url(r'^payment_type_create/', payment_type_view.PaymentTypeView.as_view(), name="payment_type_create"),
    url(r'^product/',product_view.Create_product.as_view(), name='product' ),
    url(r'^product_detail/(?P<pk>[0-9]+)/$',ProductDetailView.as_view(), name='product_detail' ),
    url(r'^product_type/', product_type_view.Create_product_type.as_view(), name='product_type'),
    url(r'^add_to_order/', add_to_order, name='add_to_order'),
    url(r'^product_type_list/', product_type_view.product_type, name='product_type_list'),
    url(r'^order_detail/$', order_detail_view.OrderDetail.as_view(), name = 'order_detail')
]
