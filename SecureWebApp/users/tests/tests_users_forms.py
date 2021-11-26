from django.test import SimpleTestCase
from users.forms import UserRegisterForm, LoginForm, UserUpdateForm


class TestsForms(SimpleTestCase):

    def test_user_register_form_no_data(self):
        form = UserRegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_login_form_no_data(self):
        form = LoginForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_user_update_form_no_data(self):
        form = UserUpdateForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
