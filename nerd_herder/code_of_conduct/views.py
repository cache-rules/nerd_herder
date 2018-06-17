from django.shortcuts import render

from nerd_herder.utils import get_asset_urls
from .models import CommitteeMember


def code_of_conduct(request):
    _, css_url = get_asset_urls()
    context = {"title": "Code of Conduct", "css_url": css_url}
    return render(request, "code_of_conduct.html", context)


def code_of_conduct_reporting_guide(request):
    _, css_url = get_asset_urls()
    context = {
        "title": "Code of Conduct",
        "css_url": css_url,
        "committee_members": CommitteeMember.objects.all(),
    }

    return render(request, "code-of-conduct-reporting-guide.html", context)


def code_of_conduct_response_playbook(request):
    _, css_url = get_asset_urls()
    context = {"title": "Code of Conduct - Response Playbook", "css_url": css_url}
    return render(request, "code-of-conduct-response-playbook.html", context)
