from django.db import models


class CommitteeMember(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    slack = models.CharField(max_length=64)

    def __str__(self):
        return self.name
