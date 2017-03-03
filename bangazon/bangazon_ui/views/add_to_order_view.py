from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from bangazon_ui.models.customer_model import Customer
from bangazon_ui.models.order_model import Order
from bangazon_ui.models.order_model import OrderProduct
from bangazon_ui.models.product_model import Product
from django.contrib.auth.decorators import login_required

@login_required
def add_to_order(request):
    """
    Method to add a product to the current user's order, even f no open order exists

    Author: Ben Marks, Ludicrous Ducks
    """
    request_data = request.POST
    current_user = request.user
    current_customer = Customer.objects.get(user=current_user.pk)
    myorder = Order.objects.get_or_create(customer=current_customer, completed=0)
    product = Product.objects.get(pk=request_data['product_pk'])
    orderproduct = OrderProduct.objects.create(order=myorder[0], product=product)

    return HttpResponseRedirect('/order_detail')
