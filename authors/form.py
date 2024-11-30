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
    first_name = forms.CharField(max_length=55)
    last_name = forms.CharField(max_length=55)

    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and len(password) < 8:
            raise forms.ValidationError(
                'Password must be at least 8 characters long'
            )
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Passwords must match')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        return user


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
