from django.test import TestCase
from django.contrib.auth.models import User
from .models import User


class UserTestCase(TestCase):
    def test_create_customer_positive(self):
        user = User.objects.create_user(username='customer', password='P@ssword123', is_customer=True)

        self.assertTrue(user.is_customer)
        self.assertFalse(user.is_performer)

    def test_create_performer_positive(self):
        user = User.objects.create_user(username='performer', password='P@ssword123', is_performer=True)

        self.assertTrue(user.is_performer)
        self.assertFalse(user.is_customer)
