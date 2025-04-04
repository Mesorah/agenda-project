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
        serializer = ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            context={'request': request}
        )


@api_view(http_method_names=['GET'])
def contact_api_detail(request, pk):
    if request.method == 'GET':
        contact = Contact.objects.filter(id=pk).first()
        serializer = ContactSerializer(instance=contact)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


@api_view(http_method_names=['GET'])
def category_api_detail(request, pk):
    if request.method == 'GET':
        category = Category.objects.filter(id=pk).first()
        serializer = CategorySerializer(instance=category)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
