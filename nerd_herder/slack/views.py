import json
import logging

from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from nerd_herder.talk_proposals.serializers import TalkProposalSerializer
from nerd_herder.talk_proposals.utils import talk_proposal_notification
from .messages import open_submit_talk_dialog, send_response

logger = logging.getLogger(__name__)


def verify_token(token):
    verification_token = settings.SLACK_VERIFICATION_TOKEN

    if verification_token is None:
        logger.error(
            "SLACK_VERIFICATION_TOKEN is not set, cannot process incoming webhooks"
        )
        return False

    if verification_token != token:
        error = f'SLACK_VERIFICATION_TOKEN: expected "{verification_token}" received "{token}"'
        logger.error(error)
        return False

    return True


COMMANDS = {"/submit-talk": lambda data: open_submit_talk_dialog(data["trigger_id"])}


def noop(_):
    pass


@api_view(["POST"])
def slash_command(request: Request):
    data = request.data.dict()

    if not verify_token(data["token"]):
        return Response({"error": "invalid token"}, status=status.HTTP_403_FORBIDDEN)

    command_name = data["command"]
    logger.info(f"Slash command triggered: {command_name}")
    command = COMMANDS.get(command_name, noop)

    try:
        command(data)
    except Exception:
        logger.exception("Error executing slash command from slack")
        return Response(
            "An error occurred while trying to process your command", status=500
        )

    return Response()


def submit_talk_action(payload):
    logger.info('Handling talk submitted via slack')
    serializer = TalkProposalSerializer(data=payload["submission"])
    serializer.is_valid(raise_exception=True)
    serializer.save()
    logger.info('Talk proposal saved')
    talk_proposal_notification(serializer.data)
    response_url = payload['response_url']
    logger.info('Responding to user')
    send_response(response_url, text='Your talk has been submitted, thank you!')


ACTIONS = {"submit_talk": submit_talk_action}


@api_view(["POST"])
def action_handler(request):
    data = request.data.dict()
    payload = json.loads(data["payload"])

    if not verify_token(payload["token"]):
        return Response({"error": "invalid token"}, status=status.HTTP_403_FORBIDDEN)

    action_name = payload["callback_id"]
    logger.info(f"Action triggered: {action_name}")
    action = ACTIONS.get(action_name, noop)

    try:
        action(payload)
    except ValidationError:
        logger.exception(f"Error executing action from slack")

    return Response()
