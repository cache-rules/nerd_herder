from django.db import transaction
from rest_framework import serializers

from nerd_herder.talks.models import Speaker, Talk


class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talk
        fields = ('id', 'title', 'description', 'talk_type', 'speakers')


class NewTalkSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    email = serializers.EmailField()
    title = serializers.CharField(max_length=128)
    description = serializers.CharField()
    talk_type = serializers.ChoiceField(Talk.TALK_TYPES)

    class Meta:
        model = Talk
        fields = ('title', 'description', 'talk_type', 'speakers')

    @transaction.atomic
    def create(self, validated_data):
        name = validated_data.get('name')
        email = validated_data.get('email')
        title = validated_data.get('title')
        description = validated_data.get('description')
        talk_type = validated_data.get('talk_type')
        speaker, _ = Speaker.objects.update_or_create(email=email, defaults={'name': name})
        talk = Talk.objects.create(title=title, description=description, talk_type=talk_type)
        talk.speakers.add(speaker)

        return validated_data

    def update(self, instance, validated_data):
        pass
