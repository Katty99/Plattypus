from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm

from Plattypus.account.models import Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email_address': 'Email Address',
            'password': 'Password',
            'birthday': 'Date of Birth',
            'profile_picture': 'Profile Picture',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email_address': forms.TextInput(attrs={'placeholder': 'Email Address'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'birthday': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }


class LoginForm(AuthenticationForm):
    email_address = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email Address"}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}), label='')

    error_messages = {
        'invalid_login': _(
            "Invalid username or password!"
        ),
        'inactive': _("This account is inactive."),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username', None)

    field_order = ['email_address', 'password']


class DeleteAccountForm(AccountForm):
    class Meta:
        model = Account
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['disabled'] = 'disabled'
