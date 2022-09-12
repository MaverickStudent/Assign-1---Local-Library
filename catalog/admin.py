from django.contrib import admin
# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language

# Comment it out on Part 4 - Advanced Configurations
# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(BookInstance)

# Register your models
# Can't directly specify the genre field in list_display because it is a ManyToManyField
# See model.py > def display_genre(self):
admin.site.register(Genre)
admin.site.register(Language)

# Inline editing of associated records
# BookInstance information inline to our Book detail by specifying inlines in your BookAdmin
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Configure list views
    list_display = ('title', 'author', 'display_genre')

    # Inline editing of associated records
    # BookInstance information inline to our Book detail by specifying inlines in your BookAdmin
    inlines = [BooksInstanceInline]

    # Will make the field visible in the Admin section,
    # allowing us to assign a User to a BookInstance when needed.
    @admin.register(BookInstance)
    class BookInstanceAdmin(admin.ModelAdmin):
        list_display = ('book', 'status', 'borrower', 'due_back', 'id')
        list_filter = ('status', 'due_back')

        fieldsets = (
            (None, {
                'fields': ('book', 'imprint', 'id')
            }),
            ('Availability', {
                'fields': ('status', 'due_back', 'borrower')
            }),
        )

# Add an inline listing of Book items to the Author detail view
class BooksInline(admin.TabularInline):
    model = Book

# Define the admin class with tuple order
class AuthorAdmin(admin.ModelAdmin):
    # Configure list views
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    # Organize detail view layout
    # Controlling which fields are displayed and laid out
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    # Add an inline listing of Book items to the Author detail view
    inlines = [BooksInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for BookInstance using the decorator
# @admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # Configure list views
    list_display = ('book', 'status', 'due_back', 'id')

    # Configure list filters
    list_filter = ('status', 'due_back')

    # Sectioning the detail view
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )







