from django.contrib import admin
from django.utils.html import format_html

from apps.management.forms import PassDBForm
from apps.management.functions import passEncr
from apps.management.models import PassDB


class PassDBAdmin(admin.ModelAdmin):
    # TODO: https://hakibenita.medium.com/how-to-add-custom-action-buttons-to-django-admin-8d266f5b0d41#.5sc9oa4yf
    form = PassDBForm
    list_display = (
        "name",
        "login",
        "decrypted_password",
        "group"
    )
    search_fields = ["name"]

    def get_queryset(self, request):
        # TODO: request.user.groups.all()
        #import pdb
        #pdb.set_trace()
        if request.user.is_superuser:
            # can be returned None to avoid superuser to access all storaged
            # passwords
            return PassDB.objects.all()
        return PassDB.objects.filter(group=request.user.groups.all().first())

    def reveal(self, obj):
        '''
        disabled becouse there\'s no need to convert values on admin
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


admin.site.register(PassDB, PassDBAdmin)
