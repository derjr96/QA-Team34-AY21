import unittest
from django.contrib.auth import get_user_model, authenticate


class Test(unittest.TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(username='Test', password='12test12', email='test@example.com')
        self.user.save()

    def tearDown(self) -> None:
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='Test', password='12test12')
        self.assertTrue(user is not None and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='Test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)
