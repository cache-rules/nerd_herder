from django.db import models

from nerd_herder.models import UUIDModel, TimeStampedModel, ContactModel


class Venue(UUIDModel, TimeStampedModel):
    name = models.TextField()
    description = models.TextField(blank=True)
    date_scheduled = models.DateTimeField(blank=True, null=True)
    address = models.TextField()
    notes = models.TextField(blank=True)
    capacity = models.IntegerField()


class VenueContact(UUIDModel, TimeStampedModel, ContactModel):
    job_title = models.TextField(null=True, blank=True)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
