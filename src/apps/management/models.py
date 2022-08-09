from django import forms
from django.contrib.auth.models import Group, User
from django.db import models

from apps.management.functions import passEncr


class PassDB(models.Model):
    # TODO: https://github.com/orenrimer/django-password-manager
    class Meta:
        verbose_name = 'Password'

    name = models.CharField(max_length=100)
    url = models.CharField(
            max_length=150,
            null=True,
            blank=True
        )
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    user = models.ForeignKey(
            User,
            on_delete=models.DO_NOTHING,
            null=True,
            blank=True
        )
    group = models.ForeignKey(
            Group,
            on_delete=models.DO_NOTHING,
            null=True,
            blank=True
        )

    def __str__(self):
        return self.name

    def save(self):
        self.password = passEncr("encrypt", self.password)
        super(PassDB, self).save()