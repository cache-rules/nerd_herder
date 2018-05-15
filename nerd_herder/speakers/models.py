from django.db import models

from nerd_herder.models import UUIDModel, TimeStampedModel


class Speaker(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=128)
    email = models.EmailField(unique=True, null=False, blank=False)
    email_confirmed = models.BooleanField(default=False)
    bio = models.TextField(null=True, blank=True)
    photo = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
