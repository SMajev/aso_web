from django import forms
from .models import Customer, User, Mechanic
from django.db.transaction import atomic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


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
        customer.user.groups.add(Group.objects.get(name='Mechanic'))
        if commit:
            customer.save()
        return user



class MechanicRegistrationForm(UserCreationForm):
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
        mechanic = Mechanic(user=user)
        mechanic.user.groups.add(Group.objects.get(name='Mechanic'))
        if commit:
            mechanic.save()
        return user


class MenagerRegistrationForm(UserCreationForm):
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
        mechanic = Mechanic(user=user)
        mechanic.user.groups.add(Group.objects.get(name='Menegment'))
        if commit:
            mechanic.save()
        return user

class AdminRegistrationForm(UserCreationForm):
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
        mechanic = Mechanic(user=user)
        mechanic.user.groups.add(Group.objects.get(name='Admin'))
        if commit:
            mechanic.save()
        return user