from django.contrib.auth.models import Group
from django.db import models

# TODO: https://github.com/vmalaga/PasswordManager

class PassDB(models.Model):
    name = models.Charfield(max_lenght=100)
    group = models.ForeigKey(Group)
