from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('rock-register')
        self.user_login_url = reverse('login')
        self.user_logout_url = reverse('logout')
        self.profile_url = reverse('profile')

    def test_rock_register(self):

        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_user_login(self):

        response = self.client.get(self.user_login_url)

        self.assertEquals(response.status_code, 200)

    def test_user_logout(self):

        response = self.client.get(self.user_logout_url)

        self.assertEquals(response.status_code, 302)

    def test_profile(self):

        response = self.client.get(self.profile_url)

        self.assertEquals(response.status_code, 302)
