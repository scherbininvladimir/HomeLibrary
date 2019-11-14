from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

from p_library.models import Book
from p_library.models import Author
from p_library.forms import AuthorForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)

def redactions(request):
    template = loader.get_template('redactions.html')
    books = Book.objects.all()
    books_by_publisher = {}
    for book in books:
        if books_by_publisher.get(book.publisher.name) is None:
            books_by_publisher[book.publisher.name] = [book]
        else:
            books_by_publisher[book.publisher.name].append(book)

    biblio_data = {
        "books_by_publisher": books_by_publisher,
        }
    return HttpResponse(template.render(biblio_data, request))

def index(request):
    template = loader.get_template('index.html')
    books_count = Book.objects.all().count()
    books = Book.objects.all()
    biblio_data = {
        "books_count": books_count,
        "books": books,
        }
    return HttpResponse(template.render(biblio_data, request))

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')

class AuthorEdit(CreateView):  
    model = Author  
    form_class = AuthorForm  
    success_url = reverse_lazy('p_library:author_list')  
    template_name = 'authors_edit.html'  
  
  
class AuthorList(ListView):  
    model = Author  
    template_name = 'authors_list.html'