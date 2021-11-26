from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import register, user_logout, profile


class TestUrls(SimpleTestCase):

    def test_register_url_is_resolved(self):
        url = reverse('rock-register')
        self.assertEquals(resolve(url).func, register)

    def test_user_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, user_logout)

    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)
