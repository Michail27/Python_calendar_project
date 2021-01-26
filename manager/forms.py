from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, Textarea, CharField, PasswordInput, Select, SelectMultiple, EmailField
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django import forms


class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'city', 'password1', 'password2')

    error_messages = {
        "password_mismatch": "Passwords do not match.",
        "email_exists": "Email addresses already present",
        "username_exists": "Username already present"}

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(self.error_messages['email_exists'])

    city = forms.CharField(required=False, widget=TextInput(attrs={"class":  "form-control"}))
    email = EmailField(required=True, widget=TextInput(attrs={"class":  "form-control"}))
    username = UsernameField(widget=TextInput(attrs={"class":  "form-control"}))
    password1 = CharField(label="Password", strip=False, widget=PasswordInput(
        attrs={'autocomplete': 'new-password', "class":  "form-control"}))
    password2 = CharField(label="Password confirmation", strip=False, widget=PasswordInput(
        attrs={'autocomplete': 'new-password', "class":  "form-control"}))

class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(label='Enter Username or Email',
                             widget=TextInput(attrs={'autofocus': True, 'class': "form-control"}))
    password = CharField(label='Password', strip=False,
                         widget=PasswordInput(attrs={'autocomplete': 'current-password', "class": "form-control"}))

