from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest

from typing import Optional

from auths.models import CustomUser

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    model = CustomUser

    list_display = [
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_superuser',
        'is_active',
    ]

    def get_readonly_fields(self, request: WSGIRequest, obj: Optional[CustomUser] = None):
        if not obj:
            return self.readonly_fields

        return self.readonly_fields + (
            'is_staff',
            'is_superuser',
            'is_active'
            )

admin.site.register(CustomUser, UserAdmin)
