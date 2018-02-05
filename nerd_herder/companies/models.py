from django.db import models

from nerd_herder.models import UUIDModel, TimeStampedModel, ContactModel


class Company(UUIDModel, TimeStampedModel):
    name = models.CharField(max_length=128)


class CompanyContact(UUIDModel, TimeStampedModel, ContactModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Venue(UUIDModel, TimeStampedModel):
    """
    We separate Venues from companies because some companies have multiple venues with different
    capacities. Other times one company will rent a venue from another company, and which will
    typically mean we will have a primary contact for the venue and a primary contact for the venue
    sponsor.
    """
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    date_scheduled = models.DateTimeField(blank=True, null=True)
    address = models.TextField()
    notes = models.TextField(blank=True)
    capacity = models.IntegerField()
