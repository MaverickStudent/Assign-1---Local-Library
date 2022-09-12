from django.urls import path
from . import views


# A view function that will be called if the URL pattern is detected:
urlpatterns = [
    # views.index, which is the function named index() in the views.py file.
    path('', views.index, name='index'),
    # index page, this path() function defines a pattern to match against the URL ('books/')
    # a view function that will be called if the URL matches
    path('books/', views.BookListView.as_view(), name='books'),
    # book-detail path the URL pattern
    # Syntax to capture the specific id of the book that we want to see
    # <converter specification:variable>
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    # URL for Generic class-based view listing books on loan to current user
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    # URL for Librarian view list of all books on loan
    path(r'borrowed/', views.LoanedBooksLibrarianListView.as_view(), name='all-books-borrowed'),
]