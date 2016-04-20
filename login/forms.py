from login.models import UserProfile
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('ccType', 'ccNumber', 'expDate', 'address', 'phone')


class UpdateUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'password')


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('ccType', 'ccNumber', 'expDate', 'address', 'phone')
