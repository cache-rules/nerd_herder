from rest_framework.serializers import ModelSerializer

from .models import TalkProposal, AudienceChoice


class AudienceChoiceSerializer(ModelSerializer):
    class Meta:
        model = AudienceChoice
        fields = ("id", "label")


class TalkProposalSerializer(ModelSerializer):
    class Meta:
        model = TalkProposal
        fields = ("id", "name", "email", "title", "description", "talk_type", "audience")
