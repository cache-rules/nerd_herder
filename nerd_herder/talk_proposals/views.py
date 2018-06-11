from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response

from nerd_herder.permissions import AuthenticatedCanGet
from nerd_herder.slack.messages import send_message
from .models import TalkProposal
from .serializers import TalkProposalSerializer


def get_talk_type_label(value):
    for talk_type in TalkProposal.TALK_TYPES:
        if talk_type[0] == value:
            return talk_type[1]

    return value


class TalkProposalList(generics.ListCreateAPIView):
    permission_classes = [AuthenticatedCanGet]
    queryset = TalkProposal.objects.all()
    serializer_class = TalkProposalSerializer

    def create(self, request, *args, **kwargs):
        data = super().create(request, *args, **kwargs).data
        title = data['title']
        name = data['name']
        talk_type = get_talk_type_label(data['talk_type'])
        description = data['description']
        channel = settings.SLACK_TALK_PROPOSAL_CHANNEL
        text = ':tada: A new talk has been submitted! :tada:'
        attachment = {
            'fallback': f'"{title}" has been submitted by {name}',
            'author_name': name,
            'title': title,
            # TODO: Add talk proposal view to frontend and link to it here
            # "title_link": "https://api.slack.com/",
            'fields': [
                {
                    'title': 'Talk Type',
                    'value': talk_type,
                    'short': True,
                },
                {
                    'title': 'Description',
                    'value': description,
                    'short': False,
                }
            ],
        }
        send_message(channel, text, [attachment])
        return Response({}, status=status.HTTP_201_CREATED)
