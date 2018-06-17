import pytest


@pytest.fixture()
def authenticated_client(client, django_user_model):
    email = "human.person@example.com"
    password = "not a robot!11!"
    django_user_model.objects.create_user(email=email, password=password)
    client.login(email=email, password=password)
    return client
