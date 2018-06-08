from django.apps import apps
from django.test import TestCase
from .apps import BugticketsConfig


class TestBugticketsConfig(TestCase):

    def test_app(self):
        self.assertEqual("bugtickets", BugticketsConfig.name)
        self.assertEqual("bugtickets", apps.get_app_config("bugtickets").name)
