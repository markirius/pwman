from django import forms
from django.contrib.auth.models import Group
from django.db import models

from apps.management.functions import passEncr


class PassDB(models.Model):
    # TODO: https://github.com/orenrimer/django-password-manager
    class Meta:
        verbose_name = 'Password'

    name = models.CharField(max_length=100)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    group = models.ForeignKey(
            Group,
            on_delete=models.DO_NOTHING,
            null=True,
            blank=True)

    def __str__(self):
        return self.name

    def save(self):
        self.password = passEncr("encrypt", self.password)
        super(PassDB, self).save()

