from django.test import SimpleTestCase
from api.views import *
from django.urls import resolve, reverse


class UrlTestCase(SimpleTestCase):

    def test_customer_info_url(self):
        url = reverse('customer-info')
        self.assertEqual(resolve(url).func, customer_info)

    def test_customer_update_url(self):
        url = reverse('customer-update')
        self.assertEqual(resolve(url).func, customer_update)

    def test_order_detail_url(self):
        url = reverse('order-detail', args=[1])
        self.assertEqual(resolve(url).func, order_detail)

    def test_signup_url(self):
        url = reverse('signup')
        self.assertEqual(resolve(url).func, customer_signup)

    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, customer_login)

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, customer_logout)
