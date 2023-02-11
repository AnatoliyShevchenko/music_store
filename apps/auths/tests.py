# Django
from django.contrib.auth.hashers import make_password
from django.test import TestCase

# Local
from .forms import LoginForm
from .models import CustomUser


class CustomUserTestCase(TestCase):

    def setUp(self):
        pass

    def test_create_user(self):
        email='user@mail.cc'
        first_name = 'brick'
        last_name = 'qwerty'
        password = make_password('12345-qwe')
        CustomUser.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )

    def test_autorization_form(self):
        data = {
            'email': 'kjnaewnj@mail.com',
            'password': '123456-qw',
        }
        form = LoginForm(data=data)
        self.assertTrue(form.is_valid())