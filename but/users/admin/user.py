from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdminModel(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (
            'username',
            'email',
            'is_active',
            'date_joined',
            'last_login',
            'id',
    )

    search_fields = [
            'username',
            'email',
            'is_active',
    ]

    list_filter = (
            'date_joined',
            'last_login',
    )
