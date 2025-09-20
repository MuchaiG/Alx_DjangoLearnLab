from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "borrower")  # ✅ fixed
    list_filter = ("published_date",)  # ✅ fixed
    search_fields = ("title", "author")

