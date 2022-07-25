import datetime
import time

from django.db import models
from django import forms

from apps.management.functions import passEncr

class PassDB(models.Model):
    # TODO: https://github.com/orenrimer/django-password-manager
    class Meta:
        verbose_name = 'Password'

    name = models.CharField(max_length=100)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save(self):
        self.password = passEncr("encrypt", self.password)
        super(PassDB, self).save()