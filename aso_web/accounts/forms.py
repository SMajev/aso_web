from django import forms
from .models import Customer, User, Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']

class ProfileForm(forms.ModelForm):
    class Meta(UserForm.Meta):
        model = Profile
        fields = '__all__'

class CustomerForm(forms.ModelForm):
    class Meta(ProfileForm.Meta):
        model = Customer
        fields = '__all__'

