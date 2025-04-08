from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.pagination import PageNumberPagination

from agenda.models import Category, Contact
from agenda.serializers import CategorySerializer, ContactSerializer


class ContactAPIPagination(PageNumberPagination):
    page_size = 5


class ContactAPIView(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    pagination_class = ContactAPIPagination


class ContactAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class CategoryAPIDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
