from rest_framework import generics, status
from rest_framework.response import Response

from nerd_herder.permissions import AuthenticatedCanGet
from .models import TalkProposal
from .serializers import TalkProposalSerializer
from .utils import talk_proposal_notification


class TalkProposalList(generics.ListCreateAPIView):
    permission_classes = [AuthenticatedCanGet]
    queryset = TalkProposal.objects.all()
    serializer_class = TalkProposalSerializer

    def create(self, request, *args, **kwargs):
        data = super().create(request, *args, **kwargs).data
        talk_proposal_notification(data)
        return Response({}, status=status.HTTP_201_CREATED)
