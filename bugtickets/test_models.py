from django.test import TestCase
from .models import BugTicket, BugUpvote, Comment


class TestBugTicketModel(TestCase):
    
    def test_str_representation(self):
        ticket = BugTicket(title="Test title", date_created="May 8, 2018", id=1)
        self.assertEqual(str(ticket), "Bug: Test title (May 8, 2018 - 1)")
        
        
class TestBugUpvoteModel(TestCase):
    def test_str_representation(self):
        upvote = BugUpvote(date_created="May 8, 2018")
        self.assertEqual(str(upvote), "(May 8, 2018)")
 

class TestCommentModel(TestCase):
    def test_str_representation(self):
        comment = Comment(date_created="May 8, 2018")
        self.assertEqual(str(comment), "(May 8, 2018)")