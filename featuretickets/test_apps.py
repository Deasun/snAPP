from django.apps import apps
from django.test import TestCase
from .apps import FeatureticketsConfig


class TestFeatureticketsConfig(TestCase):

    def test_app(self):
        self.assertEqual("featuretickets", FeatureticketsConfig.name)
        self.assertEqual("featuretickets", apps.get_app_config("featuretickets").name)