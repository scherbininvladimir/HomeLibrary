from django.contrib import admin
from p_library.models import Book
from p_library.models import Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

@admin.register(Author)
class Author(admin.ModelAdmin):
    pass