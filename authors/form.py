from django import forms
from django.contrib.auth.models import User
from password_strength import PasswordPolicy


password_policy = PasswordPolicy.from_names(
    length=8,
    uppercase=2,
    numbers=2,
    special=2,
    nonletters=2,
)


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(min_length=5, max_length=55)
    last_name = forms.CharField(min_length=5, max_length=55)

    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')

        user_exists = User.objects.filter(username=username).exists()

        if user_exists:
            self.add_error('username', 'This username already exists')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        email_exists = User.objects.filter(email=email).exists()

        if email_exists:
            self.add_error('email', 'This email already exists')

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')

        errors = password_policy.test(password)
        if errors:
            error_messages = [str(error) for error in errors]
            self.add_error('password', ' '.join(error_messages))

        return password

    def clean(self):
        cleaned_data = super().clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error('password', 'Passwords need to be the same')

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if not username or not password:
            if not username:
                self.add_error('username', 'Username is required.')
            if not password:
                self.add_error('password', 'Password is required.')

        return cleaned_data
