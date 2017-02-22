from django.conf.urls import url
from . import views

app_name = 'bangazon_ui_app'
urlpatterns = [
url(r'^list$', views.home, name="home"),
url(r'^register/$', views.register_view.Register, name='register'),
url(r'^login/$', views.login_view.Login, name='login'),
url(r'^logout/$', views.login_view.logout_user, name="logout"),
]