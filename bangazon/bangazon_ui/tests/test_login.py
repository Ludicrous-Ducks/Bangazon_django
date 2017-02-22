from django.test import TestCase
import sys
sys.path.append('../')
from bangazon_ui.views.login_view import Login
from django.contrib.auth.models import User

class LogInTestCase(TestCase):
	def test_login_view_with_username_password(self):

		create_user(username = "jkc", password="jkc123456")
		self.client.get(reverse('bangazon_ui:login'))
		return response