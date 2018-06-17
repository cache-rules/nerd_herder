from django.urls import path

from .views import slash_command, action_handler

app_name = "slack"

urlpatterns = [
    path("slash-command", slash_command, name="slash_command"),
    path("action", action_handler, name="action"),
]
