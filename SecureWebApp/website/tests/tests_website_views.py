from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.rock_home_url = reverse('rock-home')
        self.update_item_url = reverse('update_item')
        self.process_order_url = reverse('process_order')
        self.rock_about_url = reverse('rock-about')
        self.rock_cart_url = reverse('rock-cart')
        self.rock_checkout_url = reverse('rock-checkout')
        self.rock_seller_url = reverse('rock-seller')
        self.seller_create_order_url = reverse('seller-create-order')
        self.update_order_url = reverse('updateorder', args=[1])
        self.delete_order_url = reverse('deleteorder', args=[1])

    def test_rock_home(self):

        response = self.client.get(self.rock_home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/home.html')

    def test_update_item(self):

        response = self.client.get(self.update_item_url)

        self.assertEquals(response.status_code, 302)

    def test_process_order(self):

        response = self.client.get(self.process_order_url)

        self.assertEquals(response.status_code, 302)

    def test_rock_about(self):

        response = self.client.get(self.rock_about_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'website/about.html')

    def test_rock_cart(self):

        response = self.client.get(self.rock_cart_url)

        self.assertEquals(response.status_code, 302)

    def test_rock_checkout(self):

        response = self.client.get(self.rock_checkout_url)

        self.assertEquals(response.status_code, 302)

    def test_rock_seller(self):

        response = self.client.get(self.rock_seller_url)

        self.assertEquals(response.status_code, 302)

    def test_seller_create_order(self):

        response = self.client.get(self.seller_create_order_url)

        self.assertEquals(response.status_code, 302)

    def test_update_order(self):

        response = self.client.get(self.update_order_url)

        self.assertEquals(response.status_code, 302)

    def test_delete_order(self):

        response = self.client.get(self.delete_order_url)

        self.assertEquals(response.status_code, 302)
