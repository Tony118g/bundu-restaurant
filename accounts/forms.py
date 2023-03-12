from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):

    email = forms.EmailField(required=True)
    first_name = forms.CharField(
                                max_length=35,
                                label='First name (up to 35 characters)'
                                )
    last_name = forms.CharField(
                                max_length=35,
                                label='Last name (up to 35 characters)'
                                )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )


class EditUserForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(
                                max_length=35,
                                label='First name (up to 35 characters)'
                                )
    last_name = forms.CharField(
                                max_length=35,
                                label='Last name (up to 35 characters)'
                                )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )
