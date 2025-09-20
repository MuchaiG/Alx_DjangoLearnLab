# bookshelf/forms.py
from django import forms
from .models import Book

class ExampleForm(forms.Form):
    """Example form to demonstrate secure input handling."""
    search_query = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Search books...'}),
        help_text="Enter the title or keyword to search."
    )

    def clean_search_query(self):
        query = self.cleaned_data['search_query']
        # Sanitize/validate input (extra layer of defense)
        if any(char in query for char in [';', '--', '"', "'"]):
            raise forms.ValidationError("Invalid characters in search query.")
        return query


class BookForm(forms.ModelForm):
    """Secure form for creating or updating Book objects."""
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']
