import logging

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Entry
from .serializers import EntrySerializer

logger = logging.getLogger(__name__)


class EntriesList(ListCreateAPIView):
    queryset = Entry.objects.all().order_by('position')
    serializer_class = EntrySerializer

    def put(self, request):
        try:
            new_order = request.data['order']
        except KeyError:
            return Response({'order': ['This field is required.']},
                            status=status.HTTP_400_BAD_REQUEST)

        for entry in Entry.objects.all():
            try:
                entry.position = new_order[str(entry.id)]
            except KeyError:
                error = f'Missing position value for entry with id "{entry.id}"'
                return Response({'order': [error]}, status=status.HTTP_400_BAD_REQUEST)

            entry.save()

        return Response({'order': new_order}, status=status.HTTP_200_OK)


class EntryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
