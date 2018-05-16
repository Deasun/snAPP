from django.test import TestCase
from .models import FeatureTicket


class TestFeatureTicketModel(TestCase):
    def test_str_representation(self):
        ticket = FeatureTicket(title="Test title", date_created="May 8, 2018")
        self.assertEqual(str(ticket), "Request: Test title (May 8, 2018)")