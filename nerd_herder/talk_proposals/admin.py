from django.contrib import admin

from .models import TalkProposal


class TalkProposalModelAdmin(admin.ModelAdmin):
    model = TalkProposal
    list_display = ("title", "created", "name", "email", "talk_type", "description")
    ordering = ('-created',)


admin.site.register(TalkProposal, TalkProposalModelAdmin)
