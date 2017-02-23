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

]