from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "Ngugi wa Thiong'o"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print("-", book.title)
except Author.DoesNotExist:
    print(f"No author found with name {author_name}")


# List all books in a library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"\nBooks in {library_name}:")
    for book in books_in_library:
        print("-", book.title)
except Library.DoesNotExist:
    print(f"No library found with name {library_name}")


# Retrieve the librarian for a library
try:
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)  # Access via related_name
    print(f"\nLibrarian for {library_name}: {librarian.name}")
except Library.DoesNotExist:
    print(f"No library found with name {library_name}")
except Librarian.DoesNotExist:
    print(f"No librarian assigned to {library_name}")
