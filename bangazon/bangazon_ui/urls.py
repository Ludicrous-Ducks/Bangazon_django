from django.conf.urls import url
import sys
sys.path.append('../')
from bangazon_ui.views import login_view


app_name = 'bangazon_ui'
urlpatterns = [
url(r'^login/$', login_view.Login.as_view(), name='login'),
url(r'^logout/$', login_view.logout_user, name="logout"),
]