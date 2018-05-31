from django.urls import path

from nerd_herder.code_of_conduct.views import code_of_conduct, code_of_conduct_reporting_guide,\
    code_of_conduct_response_playbook

app_name = 'code_of_conduct'

urlpatterns = [
    path('', code_of_conduct),
    path('reporting-guide', code_of_conduct_reporting_guide),
    path('response-playbook', code_of_conduct_response_playbook),
]
