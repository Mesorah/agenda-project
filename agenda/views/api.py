from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from agenda.models import Category, Contact
from agenda.serializers import CategorySerializer, ContactSerializer


@api_view(http_method_names=['GET', 'POST'])
def contact_api(request):
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(
            instance=contacts,
            many=True,
            context={'request': request}
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    elif request.method == 'POST':
        serializer = ContactSerializer(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )


@api_view(http_method_names=['GET', 'PATCH', 'DELETE'])
def contact_api_detail(request, pk):
    contact = get_object_or_404(Contact, id=pk)

    if request.method == 'GET':
        serializer = ContactSerializer(
            instance=contact,
            context={'request': request}
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
        )

    elif request.method == 'PATCH':
        serializer = ContactSerializer(
            instance=contact,
            data=request.data,
            partial=True,
            context={'request': request}
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    elif request.method == 'DELETE':
        contact.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(http_method_names=['GET'])
def category_api_detail(request, pk):
    if request.method == 'GET':
        category = Category.objects.filter(id=pk).first()
        serializer = CategorySerializer(instance=category)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
