from django.contrib import admin
from django.utils.html import format_html

from apps.management.forms import PassDBForm
from apps.management.functions import passEncr
from apps.management.models import PassDB
from django.db.models import Q

class PassDBAdmin(admin.ModelAdmin):
    # TODO: https://hakibenita.medium.com/how-to-add-custom-action-buttons-to-django-admin-8d266f5b0d41#.5sc9oa4yf
    form = PassDBForm
    list_display = (
        "name",
        "url",
        "login",
        "decrypted_password",
        "group"
    )
    search_fields = ["name"]

    def get_queryset(self, request):
        if request.user.is_superuser:
            # can be returned None to avoid superuser to access all storaged
            # passwords
            return None
        return PassDB.objects.filter(
                Q(group__in=request.user.groups.all()) | Q(user=request.user)
            );

    def reveal(self, obj):
        '''
        disabled because there\'s no need to convert values on admin
        '''
        return format_html(
            '''
            <a class="button" href="javascript:alert('Conta: {}
            \\nSenha: {}');">Password</a>
            ''',
            obj.login,
            passEncr('decrypt', obj.password)
        )

    def decrypted_password(self, obj):
        return passEncr('decrypt', obj.password)

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
            obj.save()
        obj.save()


admin.site.register(PassDB, PassDBAdmin)
