from django.contrib import admin  
from django.urls import path, reverse_lazy  
from django.contrib.auth.views import LoginView, LogoutView
from allauth.account.views import login, logout

from .views import index, AuthorEdit, AuthorList, author_create_many, books_authors_create_many, lended_books, return_lended_book, lend, add_mate, RegisterView, CreateUserProfile

app_name = 'p_library'  
urlpatterns = [
    path('', index, name='index'),  
    path('author/create', AuthorEdit.as_view(), name='author_create'),  
    path('authors', AuthorList.as_view(), name='author_list'),  
    path('author/create_many', author_create_many, name='author_create_many'),
    path('author_book/create_many', books_authors_create_many, name='author_book_create_many'),
    path('lended_books/', lended_books, name='lended_books_list'),
    path('lended_books/lend', lend),
    path('lended_books/return', return_lended_book),
    path('lended_books/add_mate', add_mate),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', RegisterView.as_view(  
        template_name='register.html',  
		success_url=reverse_lazy('p_library:profile-create')  
    ), name='register'),  
    path('profile-create/', CreateUserProfile.as_view(), name='profile-create'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
