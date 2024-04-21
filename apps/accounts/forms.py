from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import User


class CustomUserCreationForm(UserCreationForm):
    is_customer = forms.BooleanField(label='Customer', required=False)
    is_performer = forms.BooleanField(label='Performer', required=False)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'is_customer', 'is_performer', 'first_name', 'last_name')

    def clean(self):
        cleaned_data = super().clean()
        is_customer = cleaned_data.get('is_customer')
        is_performer = cleaned_data.get('is_performer')

        if not is_customer and not is_performer:
            raise ValidationError("Необходимо выбрать один из вариантов.")
