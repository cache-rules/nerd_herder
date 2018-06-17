from django.conf import settings

from nerd_herder.slack.messages import send_message
from nerd_herder.talk_proposals.models import TalkProposal


def get_talk_type_label(value):
    for talk_type in TalkProposal.TALK_TYPES:
        if talk_type[0] == value:
            return talk_type[1]

    return value


def talk_proposal_notification(data):
    title = data["title"]
    name = data["name"]
    talk_type = get_talk_type_label(data["talk_type"])
    description = data["description"]
    channel = settings.SLACK_TALK_PROPOSAL_CHANNEL
    text = ":tada: A new talk has been submitted! :tada:"
    attachment = {
        "fallback": f'"{title}" has been submitted by {name}',
        "author_name": name,
        "title": title,
        # TODO: Add talk proposal view to frontend and link to it here
        # "title_link": "https://api.slack.com/",
        "fields": [
            {"title": "Talk Type", "value": talk_type, "short": True},
            {"title": "Description", "value": description, "short": False},
        ],
    }
    send_message(channel, text, [attachment])
