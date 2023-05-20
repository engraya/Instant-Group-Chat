from django.test import TestCase
from django.test import SimpleTestCase
# Create your tests here.


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_page_status_code(self):
        response = self.client.get('/loginPage/')
        self.assertEqual(response.status_code, 200)


    def test_register_page_status_code(self):
        response = self.client.get('/registerPage/')
        self.assertEqual(response.status_code, 200)

    def test_profile_page_status_code(self):
        response = self.client.get('/profilePage/')
        self.assertEqual(response.status_code, 200)
        


