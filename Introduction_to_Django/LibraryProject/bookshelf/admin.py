from .models import Book

from .models import Book

# Custom admin class for the Book model
class BookAdmin(admin.ModelAdmin):
    """
    Customizes the Django admin interface for the Book model.
    """
    # Displays specified fields in the list view of the admin
    list_display = ('title', 'author', 'publication_year')

    # Adds filters to the right-hand sidebar for these fields
    list_filter = ('publication_year',)

    # Enables search functionality for the specified fields
    search_fields = ('title', 'author')

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)
