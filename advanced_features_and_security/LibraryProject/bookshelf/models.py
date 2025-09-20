from django.db import models

class Book(models.Model):
    """
    A model to represent a book in the bookshelf application.
    
    Fields:
    - title: The title of the book.
    - author: The author of the book.
    - publication_year: The year the book was published.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        """
        Returns a string representation of the Book object.
        """
        return f"{self.title} by {self.author} ({self.publication_year})"
