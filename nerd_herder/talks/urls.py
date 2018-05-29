from django.urls import path

from nerd_herder.talks.views import TalkList

app_name = 'talks'

urlpatterns = [
    path('', TalkList.as_view(), name='talk_list'),
]
