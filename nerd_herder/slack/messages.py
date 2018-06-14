import json
import logging

from django.conf import settings
from slackclient import SlackClient

from nerd_herder.talk_proposals.models import TalkProposal

logger = logging.getLogger(__name__)


def get_client() -> SlackClient:
    """
    Instantiates a slack client based on the site settings.

    Returns:
        SlackClient
    """
    token = settings.SLACK_BOT_USER_TOKEN

    if token is None:
        logger.warning('Unable to send slack message: SLACK_BOT_USER_TOKEN not set.')
        return None

    return SlackClient(token)


def send_message(channel: str, text: str, attachments: list = None) -> None:
    """
    Sends a message to the slack channel of your choice. Does not attempt to send a message if the
    SLACK_BOT_USER_TOKEN environment variable is not set.

    Args:
        channel: The channel to post to
        text: The text to post
        attachments: The attachments to post. See the slack documentation for details:
            https://api.slack.com/docs/message-attachments

    Returns:
        None
    """
    client = get_client()

    if client is None:
        return

    bot_name = settings.SLACK_BOT_NAME
    bot_emoji = settings.SLACK_BOT_EMOJI
    response = client.api_call(
        'chat.postMessage',
        channel=channel,
        text=text,
        username=bot_name,
        icon_emoji=f':{bot_emoji}:',
        attachments=attachments,
    )

    if response['ok'] is False:
        error = response['error']
        logger.error(f'Error sending message to slack: {error}')

        if error == 'channel_not_found':
            logger.error(f'The slack bot may not have been invited to the channel {channel}')


def open_submit_talk_dialog(trigger_id) -> None:
    client = get_client()

    if client is None:
        return

    talk_types = [{'label': tt[1], 'value': tt[0]} for tt in TalkProposal.TALK_TYPES]
    dialog = {
        'title': 'Submit a talk',
        'callback_id': 'submit_talk',
        'elements': [
            {
                'label': 'Name',
                'name': 'name',
                'type': 'text',
                'placeholder': 'Grace Hopper',
            },
            {
                'label': 'Email',
                'name': 'email',
                'type': 'text',
                'subtype': 'email',
                'placeholder': 'you@example.com',
            },
            {
                'label': 'Talk title',
                'name': 'title',
                'type': 'text',
            },
            {
                'label': 'Talk description',
                'name': 'description',
                'type': 'textarea',
            },
            {
                'label': 'Talk type',
                'name': 'talk_type',
                'type': 'select',
                'options': talk_types,
            },
        ]
    }

    response = client.api_call('dialog.open', trigger_id=trigger_id, dialog=json.dumps(dialog))

    if response['ok'] is False:
        error = response['error']
        logger.error(f'Error opening dialog with slack: {error}')
