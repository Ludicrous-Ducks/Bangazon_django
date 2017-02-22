from django.test import TestCase
import sys
sys.path.append('../')
from bangazon_ui.views.login_view import Login
from django.contrib.auth.models import User
from django.urls import reverse


class TestCaseLogin(TestCase):
	def test_login_view_with_username_password(self):

		user_test = User.objects.create_user(username = "jkc", password="jkc123456")
		user = {'username': "jkc", "password": "jkc12345678"}
		response = self.client.post(reverse('bangazon_ui:login'), user)
		
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response.url, "/")