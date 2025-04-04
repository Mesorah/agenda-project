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

    def validate_first_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError(
                'O primeiro nome deve conter apenas letras.'
            )
        if len(value) < 2:
            raise serializers.ValidationError(
                'O primeiro nome deve ter pelo menos 2 caracteres.'
            )
        return value

    def validate_last_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError(
                'O sobrenome deve conter apenas letras.'
            )
        if len(value) < 2:
            raise serializers.ValidationError(
                'O sobrenome deve ter pelo menos 2 caracteres.'
            )
        return value

    def validate_description(self, value):
        if len(value) > 500:
            raise serializers.ValidationError(
                'A descrição deve ter no máximo 500 caracteres.'
            )
        return value
