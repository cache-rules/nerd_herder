from django.contrib import admin

# Register your models here.
from nerd_herder.speakers.models import Speaker, Talk

admin.site.register(Speaker)
admin.site.register(Talk)
