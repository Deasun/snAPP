from django.test import TestCase
from .models import Order, OrderLineItem


class TestOrder(TestCase):
    def test_str_representation(self):
        order = Order(id=1, date="May 8, 2018", full_name="Test Tester")
        self.assertEqual(str(order), "{0}-{1}-{2}".format(order.id, order.date, order.full_name))

class TestOrderLineItem(TestCase):
    def test_str_representation(self):
        order_item = OrderLineItem(id=2, quantity=3)
        self.assertEqual(str(order_item), "Item {0} x {1}".format(order_item.id, order_item.quantity))