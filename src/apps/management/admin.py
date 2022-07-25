from django.contrib import admin
from apps.management.models import PassDB
from apps.management.forms import PassDBForm
from django.utils.html import format_html
from apps.management.functions import passEncr


@admin.action(description='Decrypt selected passwords')
def decrypt(modeladmin, request, queryset):
    import pdb
    pdb.set_trace()
    queryset.update(password=passEncr("decrypt", queryset))

class PassDBAdmin(admin.ModelAdmin):
    # TODO: https://hakibenita.medium.com/how-to-add-custom-action-buttons-to-django-admin-8d266f5b0d41#.5sc9oa4yf
    form = PassDBForm
    list_display = (
        "name",
        "login",
        "password"
    )
    actions = [decrypt]
    search_fields = ["name"]

admin.site.register(PassDB, PassDBAdmin)