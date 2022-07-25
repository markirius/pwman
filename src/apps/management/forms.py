from django.forms import PasswordInput, ModelForm
from apps.management.models import PassDB


class PassDBForm(ModelForm):
    class Meta:
        model = PassDB
        widgets = {
            "password": PasswordInput(),
        }
        fields = ["name", "login", "password"]