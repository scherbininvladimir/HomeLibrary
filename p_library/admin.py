from django.contrib import admin
from p_library.models import Book, Author, Publisher, Mate

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name
    list_display = ('title', 'author_full_name', 'publisher')
    #fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price')

@admin.register(Author)
class Author(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class Publisher(admin.ModelAdmin):
    pass

@admin.register(Mate)
class Mate(admin.ModelAdmin):
    pass