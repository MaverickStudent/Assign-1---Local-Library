# Shortcut function to generate an HTML file using a template and data
from django.shortcuts import render
# to use a class-based generic list view
from django.views import generic
from .models import Book, Author, BookInstance, Genre, Language
# User login Required for function-based views
from django.contrib.auth.decorators import login_required
#User login Required for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin
# Provide Only Permission for librarians
from django.contrib.auth.mixins import PermissionRequiredMixin

# User login Required
@login_required
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # all - Available books (status = 'f')
    num_genres = Genre.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres' : num_genres,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

# Use a class-based generic list view
# First this generic view will query the database to get all records for the specified model (Book) then
# Render a template located at /locallibrary/catalog/templates/catalog/book_list.html
# User login required
# Ex. class MyView(LoginRequiredMixin, View):
class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    # To add pagination
    paginate_by = 10
# View (Class Based)
class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book
class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author

# Generic class-based view listing books on loan to current user
class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

# Librarian view list of all books on loan
class LoanedBooksLibrarianListView(PermissionRequiredMixin, generic.ListView):
    model = BookInstance
    permission_required = 'catalog.can_mark_returned'
    template_name = 'catalog/bookinstance_list_borrowed_librarian.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')