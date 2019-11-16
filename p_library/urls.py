from django.contrib import admin  
from django.urls import path  
from .views import AuthorEdit, AuthorList, author_create_many, books_authors_create_many, lended_books, return_lended_book, lend
  
app_name = 'p_library'  
urlpatterns = [  
    path('author/create', AuthorEdit.as_view(), name='author_create'),  
    path('authors', AuthorList.as_view(), name='author_list'),  
    path('author/create_many', author_create_many, name='author_create_many'),
    path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),
    path('lended_books/', lended_books, name='lended_books_list'),
    path('lended_books/lend', lend),
    path('lended_books/return', return_lended_book),
]
