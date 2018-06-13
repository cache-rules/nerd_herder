import json

import pytest
from django.test import Client

REQUIRED_ERROR = ['This field is required.']
NULL_ERROR = ['This field may not be null.']
NOT_AUTHENTICATED_ERROR = {'detail': 'Authentication credentials were not provided.'}
FIELDS = ['name', 'email', 'title', 'talk_type', 'description']
NAME = 'Human Person'
EMAIL = 'human.person@example.com'
TITLE = 'Things Human People Give Talks About'
TYPE = 'lightning'
DESCRIPTION = (
    "I am a human person and I have human person interests maybe you do too. I'm going to talk "
    "about a few of my human interests hopefully they also interest you."
)


@pytest.mark.django_db
def test_create_talk_proposal(mocker):
    send_message = mocker.patch('nerd_herder.talk_proposals.views.send_message')
    client = Client()
    payload = json.dumps({
        'name': NAME,
        'email': EMAIL,
        'title': TITLE,
        'talk_type': TYPE,
        'description': DESCRIPTION,
    })
    req = client.post('/api/v1/talk-proposals/', payload, content_type='application/json')

    assert {} == req.json()
    assert 201 == req.status_code
    send_message.assert_called_once()


@pytest.mark.django_db
@pytest.mark.parametrize("payload,expected", [
    ({}, {field: REQUIRED_ERROR for field in FIELDS}),
    ({field: None for field in FIELDS}, {field: NULL_ERROR for field in FIELDS}),
])
def test_create_talk_bad(client, payload, expected):
    req = client.post('/api/v1/talk-proposals/', json.dumps(payload), 'application/json')

    assert 400 == req.status_code
    assert expected == req.json()


@pytest.mark.django_db
def test_get_talk_proposals_unauthenticated(client):
    req = client.get('/api/v1/talk-proposals/')

    assert 403 == req.status_code
    assert NOT_AUTHENTICATED_ERROR == req.json()


@pytest.mark.django_db
def test_get_talk_proposals_authenticated(authenticated_client):
    req = authenticated_client.get('/api/v1/talk-proposals/')

    assert 200 == req.status_code
    assert [] == req.json()
