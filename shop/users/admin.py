from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth import get_user_model


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ['email', 'username']

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'name',
                    'surname',
                    'email',
                    'phone_number',
                    'birth_date',
                )
            }
        )
    )

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'name',
                    'surname',
                    'phone_number',
                    'birth_date',
                )
            }
        )
    )

# admin.site.register(CustomUser, CustomUserAdmin)
