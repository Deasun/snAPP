from django.test import TestCase
from .models import BugTicket


class TestBugTicketModel(TestCase):
    def test_str_representation(self):
        ticket = BugTicket(title="Test title", date_created="May 8, 2018", id=1)
        self.assertEqual(str(ticket), "Bug: {} ({} - {})".format(ticket.title, ticket.date_created, ticket.id))