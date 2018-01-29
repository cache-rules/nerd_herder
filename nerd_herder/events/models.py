from django.db import models

from nerd_herder.models import UUIDModel, TimeStampedModel
from nerd_herder.speakers.models import Talk
from nerd_herder.venues.models import Venue, VenueContact


class Sponsor(UUIDModel, TimeStampedModel):
    name = models.TextField()


class SponsorContact(UUIDModel, TimeStampedModel):
    name = models.TextField()
    email = models.EmailField(blank=False, null=False)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE, related_name='contacts')


class Event(UUIDModel, TimeStampedModel):
    name = models.TextField()
    description = models.TextField(blank=True)
    date_scheduled = models.DateTimeField(blank=True, null=True)
    rsvp_max = models.IntegerField()
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.SET_NULL)
    primary_contact = models.ForeignKey(VenueContact, blank=True, null=True,
                                        on_delete=models.SET_NULL)
    sponsors = models.ManyToManyField(Sponsor, through='EventSponsorship')
    talks = models.ManyToManyField(Talk)


class EventSponsorship(UUIDModel, TimeStampedModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    amount = models.FloatField(null=True, blank=True)
    primary_contact = models.ForeignKey(SponsorContact, blank=True, null=True,
                                        on_delete=models.SET_NULL)
    description = models.TextField()
