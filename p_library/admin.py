from django.contrib import admin
from p_library.models import Book
from p_library.models import Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name
    list_display = ('title', 'author_full_name')
    #fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price')

@admin.register(Author)
class Author(admin.ModelAdmin):
    pass