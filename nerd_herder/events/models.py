from django.db import models

from nerd_herder.companies.models import Company, CompanyContact, Venue
from nerd_herder.models import UUIDModel, TimeStampedModel, ContactModel
from nerd_herder.speakers.models import Talk


class Event(UUIDModel, TimeStampedModel):
    name = models.TextField()
    description = models.TextField(blank=True)
    date_scheduled = models.DateTimeField(blank=True, null=True)
    rsvp_max = models.IntegerField()
    talks = models.ManyToManyField(Talk, through='TalkInvitation')

    def __str__(self):
        return self.name


class Sponsorship(models.Model):
    event = models.ForeignKey(Event, null=True, blank=True, on_delete=models.SET_NULL)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # The contact is the person you would reach out to in order to get payment details
    contact = models.ForeignKey(CompanyContact, null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    value = models.FloatField()


class VenueSponsorship(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    # The sponsor contact is the main contact we have for the sponsor, they're the person you
    # contact to get payment details.
    sponsor_contact = models.ForeignKey(
        CompanyContact,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='venue_sponsorships'
    )

    # The venue contact is the main contact we have for the venue they're who you contact if you
    # have questions about the venue.
    venue_contact = models.ForeignKey(
        CompanyContact,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='venue_contacts'
    )


class TalkInvitation(UUIDModel, TimeStampedModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    talk = models.ForeignKey(Talk, on_delete=models.CASCADE)
    invited_on = models.DateTimeField(auto_now_add=True)
    accepted_on = models.DateTimeField(blank=True, null=True)
    declined_on = models.DateTimeField(blank=True, null=True)
