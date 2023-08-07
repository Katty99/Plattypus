from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from Plattypus.finances.models import Income

UserModel = get_user_model()


class LoginUserForm(auth_forms.AuthenticationForm):
    email_address = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Email Address"}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}), label='')


class RegisterUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'username', 'date_of_birth', 'email', 'password1', 'password2',
                  'profile_picture', 'gender']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Enter username',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email address',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'YYYY-MM-DD',
                    'min': '1920-01-01',
                }
            ),
        }

    def save(self, commit=True):
        result = super().save(commit)
        return result


class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'profile_picture', 'email', 'date_of_birth']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter description',
                    'rows': 3,
                },
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'YYYY-MM-DD',
                    'min': '1920-01-01',
                }
            )
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()

        return self.instance

    class Meta:
        model = UserModel
        fields = ()