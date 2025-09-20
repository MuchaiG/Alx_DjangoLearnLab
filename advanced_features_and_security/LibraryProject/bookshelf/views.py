from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Example placeholder
    return HttpResponse("Book created (dummy response)")

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return HttpResponse(f"Editing {book.title} (dummy response)")

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return HttpResponse(f"Deleted {book.title} (dummy response)")

def search_books(request):
    results = []
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['search_query']
            # Secure ORM query (prevents SQL injection)
            results = Book.objects.filter(title__icontains=query)
    else:
        form = ExampleForm()

    return render(request, "bookshelf/book_list.html", {
        "form": form,
        "results": results
    })
