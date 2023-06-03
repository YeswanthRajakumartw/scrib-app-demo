from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    USER_CHOICES = [('volunteer', 'Volunteer'), ('physically_challenged', 'Physically Challenged User'), ]
    user_type = forms.ChoiceField(choices=USER_CHOICES)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'user_type',)
