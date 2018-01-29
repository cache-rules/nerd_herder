from django.db import models

from nerd_herder.models import UUIDModel, TimeStampedModel


class Venue(UUIDModel, TimeStampedModel):
    name = models.TextField()
    description = models.TextField(blank=True)
    date_scheduled = models.DateTimeField(blank=True, null=True)
    address = models.TextField()
    notes = models.TextField(blank=True)
    capacity = models.IntegerField()


class VenueContact(UUIDModel, TimeStampedModel):
    name = models.TextField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    job_title = models.TextField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
