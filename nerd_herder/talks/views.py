from rest_framework import generics, status
from rest_framework.response import Response

from nerd_herder.permissions import AuthenticatedCanGet
from nerd_herder.talks.models import Talk
from nerd_herder.talks.serializers import TalkSerializer, NewTalkSerializer


class TalkList(generics.ListCreateAPIView):
    permission_classes = [AuthenticatedCanGet]
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TalkSerializer
        elif self.request.method == 'POST':
            return NewTalkSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({}, status=status.HTTP_201_CREATED)


class TalkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer
