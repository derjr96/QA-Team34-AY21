from django.test import SimpleTestCase
from django.urls import reverse, resolve
from website.views import home, updateItem, processOrder, about, cart, checkout, seller, createProduct, updateProduct, deleteProduct


class TestUrls(SimpleTestCase):

    def test_rock_home_url_is_resolved(self):
        url = reverse('rock-home')
        self.assertEquals(resolve(url).func, home)

    def test_update_item_url_is_resolved(self):
        url = reverse('update_item')
        self.assertEquals(resolve(url).func, updateItem)

    def test_process_order_url_is_resolved(self):
        url = reverse('process_order')
        self.assertEquals(resolve(url).func, processOrder)

    def test_rock_about_url_is_resolved(self):
        url = reverse('rock-about')
        self.assertEquals(resolve(url).func, about)

    def test_rock_cart_url_is_resolved(self):
        url = reverse('rock-cart')
        self.assertEquals(resolve(url).func, cart)

    def test_rock_checkout_url_is_resolved(self):
        url = reverse('rock-checkout')
        self.assertEquals(resolve(url).func, checkout)

    def test_rock_seller_url_is_resolved(self):
        url = reverse('rock-seller')
        self.assertEquals(resolve(url).func, seller)

    def test_seller_create_order_url_is_resolved(self):
        url = reverse('seller-create-order')
        self.assertEquals(resolve(url).func, createProduct)

    def test_update_order_url_is_resolved(self):
        url = reverse('updateorder', args=[1])
        self.assertEquals(resolve(url).func, updateProduct)

    def test_delete_order_url_is_resolved(self):
        url = reverse('deleteorder', args=[1])
        self.assertEquals(resolve(url).func, deleteProduct)
