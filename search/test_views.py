# from django.test import TestCase
# from django.test import Client
# from django.contrib.auth import get_user_model
# from django.contrib.messages import get_messages
# from django.urls import reverse
# from django.contrib.auth.models import User
# from accounts.models import Profile
# from checkout.models import Order, OrderLineItem
# from featuretickets.models import FeatureTicket
# from bugtickets.models import BugTicket


# """
# Test Search
# """
# class TestSearch(TestCase):

#     """Simulate user, bug/featuretickets and alert for search tests"""   
#     def setUp(self):
#         self.user = User.objects.create_user('Tested', 'tested@mail.com', 'q0w9e8r7t7')
#         self.user.save()
#         login = self.client.login(username='Tested', password='q0w9e8r7t7')
#         feature = FeatureTicket.objects.create(
#                 title='feature', 
#                 feature_type='Design', 
#                 description='this is a feature',
#                 created_by_id = 1
#                 )
#         bug = BugTicket.objects.create(
#                 title='bug', 
#                 bug_type='Syntax', 
#                 description='this is a bug',
#                 created_by_id = 1
#                 )
#         alert = Profile.objects.create(
#                 user_id= 1,
#                 alert="This is a new alert",
#                 alert_date='2018-06-16'
#                 )
    
#     """Test feature search status code and page render"""
#     def test_feature_search(self):
#         response = self.client.get("/search/feature/?q={0}".format("feature"))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "feature_listing.html")    
    
#     """Test feature search with no matching results"""
#     def test_feature_search_no_match(self):
#         response = self.client.get("/search/feature/?q={0}".format("2feature2"))
#         self.assertEqual(response.status_code, 200)
#         messages = list(get_messages(response.wsgi_request))
#         self.assertEqual(len(messages), 1)
#         self.assertEqual(str(messages[0]), "Your search returned no results. Please try again.")
        
#     """Test bug search status code and page render"""
#     def test_bug_search(self):
#         response = self.client.get("/search/bug/?q={0}".format("bug"))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "bug_listing.html")
    
#     """Test feature search with no matching results"""
#     def test_bug_search_no_match(self):
#         response = self.client.get("/search/bug/?q={0}".format("2bug2"))
#         self.assertEqual(response.status_code, 200)
#         messages = list(get_messages(response.wsgi_request))
#         self.assertEqual(len(messages), 1)
#         self.assertEqual(str(messages[0]), "Your search returned no results. Please try again.")
    
#     """Test member search status code and page render"""
#     def test_member_search(self):
#         response = self.client.get("/search/member_search/?q={0}".format("Tested"))
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, '/accounts/profile/1')    
    
#     """Test member search with no matches"""
#     def test_member_search_no_match(self):
#         response = self.client.get("/search/member_search/?q={0}".format("Tested"))
#         messages = list(get_messages(response.wsgi_request))
#         self.assertEqual(len(messages), 1)
#         self.assertEqual(str(messages[0]), "There are no snAPP members with that username. Please try again.")
    
#     """Test alert search status code amd render page"""
#     def test_alert_search(self):
#         response = self.client.get("/search/alert/?q={0}".format("alert"))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "profile.html")  
    
#     """Test alert search with no matches"""
#     def test_alert_search_no_match(self):
#         response = self.client.get("/search/alert/?q={0}".format("2alert2"))
#         self.assertEqual(response.status_code, 200)
#         messages = list(get_messages(response.wsgi_request))
#         self.assertEqual(len(messages), 1)
#         self.assertEqual(str(messages[0]), "Your search returned no results. Please try again.")