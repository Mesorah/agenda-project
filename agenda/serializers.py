from rest_framework import serializers

from agenda.models import Contact

# 'first_name', 'last_name', 'phone', 'email',
#             'date_created', 'description', 'category', 'cover',
#             'user'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
