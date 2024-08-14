from django import forms
# from django.contrib.auth.models import User
from agenda.models import Contact


class AddForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category',
            'cover',
        ]
