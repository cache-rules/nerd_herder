import logging

from django.conf import settings
from slackclient import SlackClient

logger = logging.getLogger(__name__)


def send_message(channel, text, attachments=None):
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
    token = settings.SLACK_BOT_USER_TOKEN

    if token is None:
        logger.warning('Unable to send slack message: SLACK_BOT_USER_TOKEN not set.')
        return

    client = SlackClient(token)
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
