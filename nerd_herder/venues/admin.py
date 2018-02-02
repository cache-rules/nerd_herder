from django.contrib import admin

# Register your models here.
from nerd_herder.venues.models import Venue, VenueContact

admin.site.register(Venue)
admin.site.register(VenueContact)
