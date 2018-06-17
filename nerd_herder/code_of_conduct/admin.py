from django.contrib import admin

from nerd_herder.code_of_conduct.models import CommitteeMember


class CommitteeMemberModelAdmin(admin.ModelAdmin):
    model = CommitteeMember
    list_display = ("name", "email", "slack")


admin.site.register(CommitteeMember, CommitteeMemberModelAdmin)
