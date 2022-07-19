import datetime
import time

from django.contrib.auth.models import Group, User
from django.core.signing import BadSignature
from django.db import models

from apps.management.functions import passEncr


class BaseSignedField(models.Field):
    def to_python(self, value):
        try:
            return passEncr('decrypt', value)
        except BadSignature:
            return value

    def get_db_prep_value(self, value, connection, prepared=False):
        return value if value is None else passEncr('encrypt', value)


class SignedCharField(BaseSignedField):
    __metaclass__ = models.SubfieldBase

    def get_internal_type(self):
        return "CharField"

    def formfield(self, **kwargs):
        defaults = {'max_length': self.max_length}
        defaults.update(kwargs)
        return super(SignedCharField, self).formfield(**defaults)


class PassDB(models.Model):
    # TODO: https://github.com/orenrimer/django-password-manager
    class Meta:
        verbose_name = 'Password'
    group = models.ForeingKey(Group)
    name = models.CharField(max_length=100)
    login = models.CharField(max_length=50)
    password = SignedCharField(max_length=100)
    server = models.CharField(max_length=60)
    uploader = models.ForeignKey(User)
    notes = models.TextField(null=True, blank=True, default="")
    creation_date = models.DateTimeField(editable=False)
    private = models.BooleanField(default=True)

    def __str__(self):
        return self.name
