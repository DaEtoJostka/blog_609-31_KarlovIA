from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class AccountViewTests(TestCase):
    def test_login_view_status_code(self):
        """
        Test that the login view returns a 200 status code.
        """
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
