from django.test import TestCase
from accounts.models import Customer, Order
import random
import string


class ModelTestCase(TestCase):
    def setUp(self):
        self.customer = Customer()
        self.customer.username = "".join(random.choices(string.ascii_lowercase, k=10))
        self.customer.email = self.customer.username + "@test.com"
        self.customer.save()

    def test_customer_fields(self):
        record = Customer.objects.get(id=1)

        self.assertEqual(record.username, self.customer.username)
        self.assertEqual(record.email, self.customer.email)


    def test_order_fields(self):
        order = Order()
        order.customer = self.customer
        order.title = "".join(random.choices(string.ascii_lowercase, k=10))
        order.items = random.randint(0, 10)
        order.save()

        record = Order.objects.get(id=1)

        self.assertEqual(order.title, record.title)
        self.assertEqual(order.items, record.items)
        self.assertEqual(order.customer, record.customer)
