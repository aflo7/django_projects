from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.views import generic


class BookDetailView(generic.DetailView):
    model = Book


class BookListView(generic.ListView):
    model = Book
    context_object_name = (
        "book_list"  # your own name for the list as a template variable
    )


# views.py is a request handler. to control what the user actually sees, use HTML templates... 

def say_hello(request):
    return render(request, "hello.html")
  
def about(request):
  return render(request, 'about.html')

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    booksThatStartWithH = Book.objects.filter(title__startswith="H").count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # this data will get inserted into the HTML template
    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
        "booksThatStartWithH": booksThatStartWithH,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)
