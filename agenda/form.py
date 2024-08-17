from django import forms
from agenda.models import Contact


class ContactForm(forms.ModelForm):
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

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        contact_id = self.instance.id

        phone_exists = Contact.objects.filter(
            phone=phone).exclude(id=contact_id).exists()

        if phone_exists:
            self.add_error('phone', 'This phone already exists')

        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        contact_id = self.instance.id

        email_exists = Contact.objects.filter(
            email=email).exclude(id=contact_id).exists()

        if email_exists:
            self.add_error('email', 'This email already exists')

        return email
