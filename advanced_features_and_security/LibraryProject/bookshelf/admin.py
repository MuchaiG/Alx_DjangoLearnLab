from django.contrib import admin
from .models import Book
from accounts.models import CustomUser, CustomUserAdmin
from django.contrib.auth.admin import UserAdmin

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "borrower")  # ✅ fixed
    list_filter = ("published_date",)  # ✅ fixed
    search_fields = ("title", "author")

@admin.site.register(CustomUser, CustomUserAdmin)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "date_of_birth", "is_staff")
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

