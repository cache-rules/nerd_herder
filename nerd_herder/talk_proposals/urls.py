from django.urls import path

from .views import AudienceChoiceList, TalkProposalList

app_name = "talk_proposals"

urlpatterns = [
    path("", TalkProposalList.as_view(), name="talk_proposal_list"),
    path("audience-choices", AudienceChoiceList.as_view(), name="audience_choice_list")
]
