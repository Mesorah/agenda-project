from django import forms
from agenda.models import Contact, Category


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

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        contact_id = self.instance.id

        phone_exists = Contact.objects.filter(
            phone=phone, user=self.user).exclude(id=contact_id).exists()

        if phone_exists:
            self.add_error('phone', 'This phone already exists')

        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        contact_id = self.instance.id

        email_exists = Contact.objects.filter(
            email=email, user=self.user).exclude(id=contact_id).exists()

        if email_exists:
            self.add_error('email', 'This email already exists')

        return email


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class RemoveCategoryFormT(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), label='Select Category to Remove')


class RemoveCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = []

    category = forms.ModelChoiceField(
        queryset=Category.objects.none(), label='Select Category to Remove')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)

        super().__init__(*args, **kwargs)

        if self.user:
            self.fields['category'].queryset = Category.objects.filter(
                user=self.user
            )


class UpdateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = []

    category = forms.ModelChoiceField(
        queryset=Category.objects.none(),  # Inicializa com queryset vazio
        label='Select Category to Update'
    )

    new_name = forms.CharField(
        max_length=55,
        required=True,
        label='New name for category'
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)

        super().__init__(*args, **kwargs)

        if self.user:
            self.fields['category'].queryset = Category.objects.filter(
                user=self.user
            )

    def save(self, commit=True):
        instance = self.cleaned_data['category']
        instance.name = self.cleaned_data['new_name']

        if commit:
            instance.save()

        return instance
