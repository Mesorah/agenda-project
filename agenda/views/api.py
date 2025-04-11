from rest_framework.generics import RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from agenda.models import Category, Contact
from agenda.serializers import CategorySerializer, ContactSerializer


class ContactAPIPagination(PageNumberPagination):
    page_size = 5


class ContactAPIViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    pagination_class = ContactAPIPagination


class CategoryAPIDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
