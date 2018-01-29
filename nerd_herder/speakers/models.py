from django.db import models

from nerd_herder.models import UUIDModel, TimeStampedModel


class Speaker(UUIDModel, TimeStampedModel):
    name = models.TextField()
    email = models.EmailField(unique=True, null=False, blank=False)
    email_confirmed = models.BooleanField(default=False)
    bio = models.TextField(null=True, blank=True)
    photo = models.URLField(null=True, blank=True)


class Talk(UUIDModel, TimeStampedModel):
    # In the future we may want to make TALK_TYPES configurable.
    TALK_TYPES = (
        ('full_length', 'Full Length (25+ minutes)'),
        ('lightning', 'Lightning Talk (5-10 minutes)')
    )

    title = models.TextField()
    description = models.TextField()
    talk_type = models.TextField(choices=TALK_TYPES)
    q_and_a = models.BooleanField(default=False)
    speakers = models.ManyToManyField(Speaker)
