from django.forms import ModelForm, PasswordInput

from apps.management.functions import passEncr
from apps.management.models import PassDB


class PassDBForm(ModelForm):
    # TODO: made password value be decrypted on form after an update

    class Meta:
        model = PassDB
        widgets = {
            "password": PasswordInput(render_value=True),
        }
        fields = ["name", "url", "login", "password", "user", "group"]
