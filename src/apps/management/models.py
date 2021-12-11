from django.contrib.auth.models import Group
from django.db import models


class Password(models.Model):
    group = models.ForeigKey(Group)
