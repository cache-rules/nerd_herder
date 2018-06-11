import logging

import requests
from django.conf import settings

logger = logging.getLogger(__name__)


def send_message(channel, text, attachments=None):
    """
    {
        "attachments": [
            {
                "fallback": "Required plain-text summary of the attachment.",
                "color": "#2eb886",
                "pretext": "Optional text that appears above the attachment block",
                "author_name": "Bobby Tables",
                "author_link": "http://flickr.com/bobby/",
                "author_icon": "http://flickr.com/icons/bobby.jpg",
                "title": "Slack API Documentation",
                "title_link": "https://api.slack.com/",
                "text": "Optional text that appears within the attachment",
                "fields": [
                    {
                        "title": "Priority",
                        "value": "High",
                        "short": false
                    }
                ],
                "image_url": "http://my-website.com/path/to/image.jpg",
                "thumb_url": "http://example.com/path/to/thumb.png",
                "footer": "Slack API",
                "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
                "ts": 123456789
            }
        ]
    }
    Args:
        channel: The channel to post to
        text: The text to post
        attachments: The attachments to post. See the slack documentation for details:
            https://api.slack.com/docs/message-attachments

    Returns:

    """
    webhook_url = settings.SLACK_WEBHOOK_URL

    if webhook_url is None:
        logger.warning('SLACK_WEBHOOK_URL not configured, cannot send slack notification')
        return

    bot_name = settings.SLACK_BOT_NAME
    bot_emoji = settings.SLACK_BOT_EMOJI

    if attachments is None:
        attachments = []

    body = {
        "channel": channel,
        "text": text,
         "link_names": 1,
        "username": bot_name,
        "icon_emoji": f':{bot_emoji}:',
        'attachments': attachments,
    }

    try:
        r = requests.post(webhook_url, json=body)
    except requests.RequestException as e:
        logger.error(f'Error sending slack notification: {e}')
        return

    if r.status_code >= 400:
        logger.error(f'Slack API returned error: {r.status_code}')
        logger.error(r.text)
