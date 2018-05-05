from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile


class TestProfileModel(TestCase):
    def test_str_representation_and_one_to_one_relationship(self):
        user = User(username="Test")
        profile = Profile(user=user)
        self.assertEqual(str(profile), "Profile of user {}".format(user.username))