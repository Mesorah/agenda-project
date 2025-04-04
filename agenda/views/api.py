from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from agenda.models import Contact
from agenda.serializers import ContactSerializer


@api_view(http_method_names=['GET'])
def contact_api(request):
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(
            instance=contacts,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
