from django.test import TestCase, Client
from django.urls import reverse

from .models import User
from .forms import CustomUserCreationForm


class UserTestCase(TestCase):
    def test_create_customer_positive(self):
        user = User.objects.create_user(username='customer', password='P@ssword123', is_customer=True)

        self.assertTrue(user.is_customer)
        self.assertFalse(user.is_performer)

    def test_create_performer_positive(self):
        user = User.objects.create_user(username='performer', password='P@ssword123', is_performer=True)

        self.assertTrue(user.is_performer)
        self.assertFalse(user.is_customer)


class RegisterViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')

    def test_register_view_get(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration.html')
        self.assertIsInstance(response.context['form'], CustomUserCreationForm)

    def test_register_view_post_success(self):
        data = {
            'username': 'customer',
            'password1': 'P@ssword123',
            'password2': 'P@ssword123',
            'is_customer': True,
            'is_performer': False
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.count(), 1)
        self.assertTrue(User.objects.filter(username='customer').exists())

    def test_register_view_post_failure(self):
        data = {
            'username': 'customer',
            'password1': 'P@ssword123',
            'password2': 'Wrongpassword123',
            'is_customer': True,
            'is_performer': False
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration.html')
        self.assertTrue('form' in response.context)
        self.assertFalse(User.objects.filter(username='customer').exists())
