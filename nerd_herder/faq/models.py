from django.db import models

from nerd_herder.models import TimeStampedModel


class Entry(TimeStampedModel):
    position = models.IntegerField()
    question = models.TextField()
    answer = models.TextField()
