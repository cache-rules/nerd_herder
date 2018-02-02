from django.contrib import admin

# Register your models here.
from nerd_herder.events.models import Sponsor, SponsorContact, Event, EventSponsorship

admin.site.register(Sponsor)
admin.site.register(SponsorContact)
admin.site.register(Event)
admin.site.register(EventSponsorship)
