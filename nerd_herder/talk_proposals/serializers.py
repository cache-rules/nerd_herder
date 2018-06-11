from rest_framework.serializers import ModelSerializer

from .models import TalkProposal


class TalkProposalSerializer(ModelSerializer):
    def create(self, validated_data):
        instance = super().create(validated_data)
        # TODO: call slack webhook
        # TODO: send email to organizers
        return instance

    class Meta:
        model = TalkProposal
        fields = ('name', 'email', 'title', 'description', 'talk_type')
