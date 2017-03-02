# from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseRedirect
# from bangazon_ui.models import order_model
# from bangazon_ui.models import payment_type_model
# from django.views.generic.base import TemplateView
# from django.contrib.auth.models import User
# from django.contrib.auth import logout, login, authenticate
# from bangazon_ui.models import customer_model
# from django.db.models import F, Sum, FloatField

# class IndexView(TemplateView)
#     """
#     Author: Ben Marks, Ludicrous Ducks
#     """
#     template_name = 'bangazon_ui/index.html'

# def get(request):
#     if self.request.user.username = "AnonymousUser":
#         message = ""
#         order_list = []
#         product_list = []
#     else:
#         customer = customer_model.Customer.objects.get(user = self.request.user.pk)
#         try:
#             order_list = order_model.Order.objects.get_or_create(customer=customer, completed = 0)
#             product_list = order_list[0].product.all()
#         except:
#             product_list = []
#         product_count = len(product_list)
#         message = "Welcome, {} {}".format(customer.user.first_name, customer.user.last_name)
#     print(message)
#     print(product_count)
#     return render(request, 'bangazon_ui/index.html', {'message': message, 'product_count': product_count})


# # def get_context_data(self, **kwargs):

# #     if self.request.user.username = "AnonymousUser":
# #         message = ""
# #         order_list = []
# #         product_list = []
# #     else:
# #         customer = customer_model.Customer.objects.get(user = self.request.user.pk)
# #         order_list = order_model.Order.objects.get_or_create(customer=customer, completed = 0)
# #         product_list = order_list[0].product.all()
# #         message = "Welcome, " + customer.user.first_name + " " + customer.user.last_name

# #     context = {'message': message, 'order_list': order_list[0], 'product_list': product_list}
# #     print(context)
# #     return context