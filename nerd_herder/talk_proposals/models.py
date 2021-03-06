from django.db import models

from nerd_herder.models import UUIDModel, TimeStampedModel


class AudienceChoice(UUIDModel, TimeStampedModel):
    label = models.CharField(max_length=128)

    def __str__(self):
        return self.label


class TalkProposal(UUIDModel, TimeStampedModel):
    # In the future we may want to make TALK_TYPES configurable.
    TALK_TYPES = (
        ("full_length", "Full Length (~25 minutes)"),
        ("lightning", "Lightning Talk (5-10 minutes)"),
    )

    name = models.CharField(max_length=128)
    email = models.EmailField(null=False, blank=False)
    title = models.CharField(max_length=128)
    description = models.TextField()
    talk_type = models.CharField(max_length=64, choices=TALK_TYPES)
    audience = models.ForeignKey(AudienceChoice, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
