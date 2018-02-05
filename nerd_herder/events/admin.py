from django.contrib import admin

# Register your models here.
from nerd_herder.events.models import Event, Sponsorship, VenueSponsorship, TalkInvitation

admin.site.register(Event)
admin.site.register(Sponsorship)
admin.site.register(VenueSponsorship)
admin.site.register(TalkInvitation)
