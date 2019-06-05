from django.contrib import admin

from .models import TalkProposal, AudienceChoice


class AudienceChoiceModelAdmin(admin.ModelAdmin):
    model = AudienceChoice
    list_display = ("label", "created")
    ordering = ("label", )


class TalkProposalModelAdmin(admin.ModelAdmin):
    model = TalkProposal
    list_display = ("title", "created", "name", "email", "talk_type", "audience", "description")
    ordering = ("-created", )


admin.site.register(AudienceChoice, AudienceChoiceModelAdmin)
admin.site.register(TalkProposal, TalkProposalModelAdmin)
