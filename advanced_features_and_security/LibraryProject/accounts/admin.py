from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    # Fields to display in the list view
    list_display = (
        "username", "email", "first_name", "last_name",
        "date_of_birth", "is_staff", "is_active"
    )
    list_filter = ("is_staff", "is_active", "date_of_birth")

    # Fieldsets when editing a user
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

    # Fieldsets when creating a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

    search_fields = ("username", "email")
    ordering = ("username",)


# Register the custom user with custom admin
admin.site.register(CustomUser, CustomUserAdmin)


