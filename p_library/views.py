from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.forms import formset_factory
from django.http.response import HttpResponseRedirect

from p_library.models import Book, Author, Mate
from p_library.forms import AuthorForm, BookForm


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
            return redirect('/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/')
            book.copy_count += 1
            book.save()
        return redirect('/')
    else:
        return redirect('/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/')
    else:
        return redirect('/')


class AuthorEdit(CreateView):  
    model = Author  
    form_class = AuthorForm  
    success_url = reverse_lazy('p_library:author_list')  
    template_name = 'authors_edit.html'  


class AuthorList(ListView):  
    model = Author  
    template_name = 'authors_list.html'


def author_create_many(request):  
    AuthorFormSet = formset_factory(AuthorForm, extra=2)  #  Первым делом, получим класс, который будет создавать наши формы. Обратите внимание на параметр `extra`, в данном случае он равен двум, это значит, что на странице с несколькими формами изначально будет появляться 2 формы создания авторов.
    if request.method == 'POST':  #  Наш обработчик будет обрабатывать и GET и POST запросы. POST запрос будет содержать в себе уже заполненные данные формы
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')  #  Здесь мы заполняем формы формсета теми данными, которые пришли в запросе. Обратите внимание на параметр `prefix`. Мы можем иметь на странице не только несколько форм, но и разных формсетов, этот параметр позволяет их отличать в запросе.
        if author_formset.is_valid():  #  Проверяем, валидны ли данные формы
            for author_form in author_formset:  
                author_form.save()  #  Сохраним каждую форму в формсете
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))  #  После чего, переадресуем браузер на список всех авторов.
    else:  #  Если обработчик получил GET запрос, значит в ответ нужно просто "нарисовать" формы.
        author_formset = AuthorFormSet(prefix='authors')  #  Инициализируем формсет и ниже передаём его в контекст шаблона.
    return render(request, 'manage_authors.html', {'author_formset': author_formset})


def books_authors_create_many(request):  
    AuthorFormSet = formset_factory(AuthorForm, extra=2)  
    BookFormSet = formset_factory(BookForm, extra=2)  
    if request.method == 'POST':  
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')  
        book_formset = BookFormSet(request.POST, request.FILES, prefix='books')  
        if author_formset.is_valid() and book_formset.is_valid():  
            for author_form in author_formset:  
                author_form.save()  
            for book_form in book_formset:  
                book_form.save()  
            return HttpResponseRedirect(reverse_lazy('p_library:author_list'))  
    else:  
        author_formset = AuthorFormSet(prefix='authors')  
        book_formset = BookFormSet(prefix='books')  
    return render(
	    request,  
		'manage_books_authors.html',  
		{  
	        'author_formset': author_formset,  
			'book_formset': book_formset,  
		}  
	)


def lended_books(request):
    template = loader.get_template('lended_books.html')
    books = Book.objects.all()
    mates = Mate.objects.all()
    biblio_data = {
        "books": books,
        "mates": mates,
        }
    return HttpResponse(template.render(biblio_data, request))


def return_lended_book(request):
    if request.method == 'POST':
        mate_id = request.POST['mate']
        book_id = request.POST['book']
        if not mate_id or not book_id:
            return redirect('/lended_books')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/lended_books')
            book.mates.remove(mate_id)
            book.save()
        return redirect('/lended_books')
    else:
        return redirect('/lended_books')

def lend(request):
    if request.method == 'POST':
        book_id = request.POST['book']
        mate_id = request.POST['mates']
        if not mate_id or not book_id:
            return redirict('lended_books')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/lended_books')
            book.mates.add(mate_id)
        return redirect('/lended_books')
    else:
        return redirect('/lended_books')