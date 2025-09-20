from django import forms
from .models import Book
from django.core.exceptions import ValidationError
import datetime

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "published_date", "borrower"]

    def clean_title(self):
        title = self.cleaned_data.get("title", "").strip()
        if not title:
            raise ValidationError("Title cannot be empty.")
        # further checks: length, disallowed characters, etc.
        return title

    def clean_published_date(self):
        date = self.cleaned_data.get("published_date")
        if date and date > datetime.date.today():
            raise ValidationError("Published date cannot be in the future.")
        return date
