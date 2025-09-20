from django.db import models
from django.conf import settings   # <- use this instead of importing User directly

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)  # <-- fix applied
    borrower = models.ForeignKey(
        settings.AUTH_USER_MODEL,   # <-- points to accounts.CustomUser
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="borrowed_books"
    )

    def __str__(self):
        return self.title

