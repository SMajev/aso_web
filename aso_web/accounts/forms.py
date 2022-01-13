from django import forms
from .models import Customer, User
from django.db.transaction import atomic
from django.contrib.auth.forms import UserCreationForm



class CustomerRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['email', 'username', 'first_name', 'last_name', 'password1', 'password2']

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Your email'
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your username'
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your name'
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your surname'
            }
        )
    )
    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        user = super().save(commit)
        customer = Customer(user=user)
        if commit:
            customer.save()
        return user






