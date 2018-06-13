from rest_framework.serializers import ModelSerializer

from .models import TalkProposal


class TalkProposalSerializer(ModelSerializer):
    class Meta:
        model = TalkProposal
        fields = ('name', 'email', 'title', 'description', 'talk_type')
