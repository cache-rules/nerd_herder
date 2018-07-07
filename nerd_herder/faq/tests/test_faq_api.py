import json

import pytest
from django.test import Client

from nerd_herder.faq.models import Entry

BASE_URL = "/api/v1/faq/"
REQUIRED_ERROR = ["This field is required."]
NULL_ERROR = ["This field may not be null."]
FIELDS = ["question", "answer", "position"]
ENTRIES = [
    {
        "question": "What version of Python should I use?",
        "answer": "Python 3 or above",
        "position": 0,
    },
    {
        "question": "Flask or Django?",
        "answer": "Whatever floats your boat",
        "position": 1,
    },
]


@pytest.mark.django_db
def test_add_entry(client: Client):
    entry = ENTRIES[0]
    payload = json.dumps(entry)
    r = client.post(BASE_URL, payload, content_type="application/json")

    assert 201 == r.status_code
    body = r.json()
    assert entry["question"] == body["question"]
    assert entry["answer"] == body["answer"]
    assert entry["position"] == body["position"]
    assert 1 == len(Entry.objects.all())


@pytest.mark.django_db
@pytest.mark.parametrize(
    "payload,expected",
    [
        ({}, {field: REQUIRED_ERROR for field in FIELDS}),
        ({field: None for field in FIELDS}, {field: NULL_ERROR for field in FIELDS}),
        ({**ENTRIES[0], "question": False}, {"question": ["Not a valid string."]}),
        ({**ENTRIES[0], "answer": False}, {"answer": ["Not a valid string."]}),
        (
            {**ENTRIES[0], "position": False},
            {"position": ["A valid integer is required."]},
        ),
    ],
)
def test_add_entry_bad(client: Client, payload, expected):
    req = client.post(BASE_URL, json.dumps(payload), "application/json")

    assert 400 == req.status_code
    assert expected == req.json()


@pytest.mark.django_db
def test_update_entry(client: Client):
    entry = Entry.objects.create(**ENTRIES[0])
    question = "I am a new title"
    url = f"{BASE_URL}{entry.id}"
    r = client.put(
        url,
        json.dumps({**ENTRIES[0], "question": question}),
        content_type="application/json",
    )
    assert 200 == r.status_code
    assert {**ENTRIES[0], "id": entry.id, "question": question} == r.json()


@pytest.mark.django_db
@pytest.mark.parametrize("field", FIELDS)
def test_update_entry_bad(client: Client, field):
    entry = Entry.objects.create(**ENTRIES[0])
    url = f"{BASE_URL}{entry.id}"

    r = client.put(
        url, json.dumps({**ENTRIES[0], field: None}), content_type="application/json"
    )

    assert 400 == r.status_code

    copy = {**ENTRIES[0]}
    copy.pop(field)
    r = client.put(url, json.dumps(copy), content_type="application/json")

    assert 400 == r.status_code

    r = client.put(
        url, json.dumps({**ENTRIES[0], field: False}), content_type="application/json"
    )

    assert 400 == r.status_code


@pytest.mark.django_db
def test_delete_entry(client: Client):
    entry = Entry.objects.create(**ENTRIES[0])
    url = f"{BASE_URL}{entry.id}"
    r = client.delete(url)

    assert 204 == r.status_code

    r = client.get(url)

    assert 404 == r.status_code


@pytest.mark.django_db
def test_get_entries(client: Client):
    for entry in ENTRIES:
        Entry.objects.create(**entry)

    r = client.get(BASE_URL, content_type="application/json")

    assert r.status_code == 200
    body = r.json()
    assert 2 == len(body)

    for idx, entry in enumerate(body):
        assert ENTRIES[idx]["question"] == entry["question"]
        assert ENTRIES[idx]["answer"] == entry["answer"]
        assert ENTRIES[idx]["position"] == entry["position"]


@pytest.mark.django_db
def test_change_entry_order(client: Client):
    entries = []

    for entry in ENTRIES:
        entries.append(Entry.objects.create(**entry))

    payload = {
        'order': {
            str(entries[0].id): 1,
            str(entries[1].id): 0,
        }
    }

    r = client.put(BASE_URL, json.dumps(payload), content_type='application/json')

    assert 200 == r.status_code
    assert payload == r.json()

    r = client.get(BASE_URL)

    assert 200 == r.status_code
    body = r.json()
    assert entries[0].id == body[1]['id']
    assert entries[1].id == body[0]['id']


@pytest.mark.django_db
def test_change_entry_order_bad(client: Client):
    entries = []

    for entry in ENTRIES:
        entries.append(Entry.objects.create(**entry))

    payload = {
        'order': {
            str(entries[0].id): 1,
        }
    }

    r = client.put(BASE_URL, json.dumps(payload), content_type='application/json')

    assert 400 == r.status_code
    assert {'order': [f'Missing position value for entry with id "{entries[1].id}"']} == r.json()

