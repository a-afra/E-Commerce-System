from django.test import TestCase, Client
from django.urls import reverse


class ViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        response = self.client.post(reverse('signup'),
                                    data={'username': 'test',
                                          'email': 'test@test.com',
                                          'password': '1234'})
        self.token = response.json()['token']

    def test_unauthorized_customer_info(self):
        response = self.client.get(reverse('customer-info'))
        self.assertEqual(response.status_code, 401)

    def test_customer_info(self):
        response = self.client.get(reverse('customer-info'),
                                   HTTP_AUTHORIZATION=f'Token {self.token}')
        self.assertEqual(response.status_code, 200)

    def test_unauthorized_customer_update(self):
        response = self.client.get(reverse('customer-update'))
        self.assertEqual(response.status_code, 401)

    def test_customer_update(self):
        response = self.client.patch(reverse('customer-update'),
                                     HTTP_AUTHORIZATION=f'Token {self.token}',
                                     data={'description': 'unit test.'},
                                     content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_unauthorized_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 401)

    def test_unauthorized_order_detail(self):
        response = self.client.get(reverse('order-detail', args=[1]))
        self.assertEqual(response.status_code, 401)

    def test_order_detail(self):
        response = self.client.get(reverse('order-detail', args=[1]),
                                   HTTP_AUTHORIZATION=f'Token {self.token}')
        self.assertEqual(response.status_code, 200)

    def test_empty_fields_customer_signup(self):
        response = self.client.post(reverse('signup'),
                                    data={'username': '',
                                          'email': '',
                                          'password': ''},
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['username'][0], 'This field may not be blank.')
        self.assertEqual(response.json()['email'][0], 'This field may not be blank.')
        self.assertEqual(response.json()['password'][0], 'This field may not be blank.')

    def test_successful_customer_login(self):
        response = self.client.post(reverse('login'),
                                    data={'username': 'test',
                                          'password': '1234'},
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_wrong_username_customer_login(self):
        response = self.client.post(reverse('login'),
                                    data={'username': '',
                                          'password': 'wrong'},
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()[0], 'Customer matching query does not exist.')

    def test_wrong_password_customer_login(self):
        response = self.client.post(reverse('login'),
                                    data={'username': 'test',
                                          'password': 'wrong'},
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()[0], 'Login credentials is invalid.')

    def test_customer_logout(self):
        response = self.client.get(reverse('logout'),
                                   HTTP_AUTHORIZATION=f'Token {self.token}')
        self.assertEqual(response.status_code, 200)
