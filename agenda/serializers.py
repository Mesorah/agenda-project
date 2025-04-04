from django.contrib.auth.models import User
from rest_framework import serializers

from agenda.models import Category, Contact


class ContactSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name',
    )

    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    class Meta:
        model = Contact
        fields = [
            'id', 'first_name', 'last_name', 'phone',
            'email', 'date_created', 'description', 'category',
            'cover', 'user'
        ]

        read_only_fields = [
            'id', 'cover', 'date_created'
        ]
