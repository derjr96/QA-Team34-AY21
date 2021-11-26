from django.test import SimpleTestCase
from website.forms import ProductForm

class TestsForms(SimpleTestCase):

    def test_product_form_valid_data(self):
        form = ProductForm(data={
            'title': 'Test Stone',
            'itemname': 'Test Stone',
            'itemprice': 25,
            'content': 'test content'
        })

        self.assertTrue(form.is_valid())

    def test_product_form_no_data(self):
        form = ProductForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)
