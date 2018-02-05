from django.contrib import admin

# Register your models here.
from nerd_herder.companies.models import Company, CompanyContact, Venue

admin.site.register(Company)
admin.site.register(CompanyContact)
admin.site.register(Venue)
