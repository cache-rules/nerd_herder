from django.urls import path

from .views import TalkProposalList

app_name = "talk_proposals"

urlpatterns = [path("", TalkProposalList.as_view(), name="talk_proposal_list")]
