import uuid

from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating created and modified fields.
    """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDModel(models.Model):
    """
    An abstract base class model that uses a UUID for the model ID instead of an auto-increment
    integer field.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class ContactModel(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(blank=False, null=False)

    class Meta:
        abstract = True
