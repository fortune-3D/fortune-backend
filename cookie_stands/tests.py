from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import CookieStand


class CookieStandTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_post = CookieStand.objects.create(
            owner=testuser1,
            location='Italy',
            description='We sell cookies',
        )
        test_post.save()

    def test_cookie_content(self):
        post = CookieStand.objects.get(id=1)
        actual_owner = str(post.owner)
        actual_location = str(post.location)
        actual_description = str(post.description)
        self.assertEqual(actual_owner, 'testuser1')
        self.assertEqual(actual_location, 'Italy')
        self.assertEqual(actual_description, 'We sell cookies')
