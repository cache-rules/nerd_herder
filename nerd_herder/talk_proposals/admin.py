from django.contrib import admin

from .models import TalkProposal


class TalkProposalModelAdmin(admin.ModelAdmin):
    model = TalkProposal
    list_display = ('title', 'name', 'email', 'talk_type', 'description', )


admin.site.register(TalkProposal, TalkProposalModelAdmin)
