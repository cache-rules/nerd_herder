from django.db import models

from nerd_herder.models import UUIDModel, TimeStampedModel
from nerd_herder.speakers.models import Speaker


class Talk(UUIDModel, TimeStampedModel):
    # In the future we may want to make TALK_TYPES configurable.
    TALK_TYPES = (
        ('full_length', 'Full Length (25+ minutes)'),
        ('lightning', 'Lightning Talk (5-10 minutes)')
    )

    title = models.CharField(max_length=128)
    description = models.TextField()
    talk_type = models.CharField(max_length=64, choices=TALK_TYPES)
    speakers = models.ManyToManyField(Speaker)

    def __str__(self):
        return self.title
