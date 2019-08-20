from django.shortcuts import render, redirect, HttpResponse
from .models import *


def index(request):
    context = {
        'books_in_db' : Books.objects.all(),
    }
    return render(request, 'authors_books/BA_index.html', context)

def bookDetail(request, id):
    context={
        'this_book' : Books.objects.get(id=id),
        'authors_of' : Books.objects.get(id=id).authors.all(),
        'these_authors' : Authors.objects.exclude(books=Books.objects.get(id=id))
    }
    return render(request, 'authors_books/book_details.html', context)

def authForm(request):
    context = {
        'auths_in_db' : Authors.objects.all(),
    }
    return render(request, 'authors_books/auth_form.html', context)

def authDetail(request, id):
    context={
        'that_author' : Authors.objects.get(id=id),
        'books_of' : Authors.objects.get(id=id).books.all(),
        'those_books' : Books.objects.exclude(authors=Authors.objects.get(id=id))
    }
    return render(request, 'authors_books/auth_details.html', context)

def creator(request):
        print(request.POST['create'])
        if request.POST['create'] == 'new_book':
            Books.objects.create(
                title=request.POST['title_input'],
                desc=request.POST['desc_input']
            )
            return redirect(f'/')
        elif request.POST['create'] == 'new_auth':
            Authors.objects.create(
                first_name=request.POST['first_input'],
                last_name=request.POST['last_input'],
                notes=request.POST['note_input']
            )
            return redirect(f'/authors')

def additionalAuthor(request):
    author_id = int(request.POST['available_authors'])
    selected_author = Authors.objects.get(id=author_id)
    book_id = int(request.POST['add_author'])
    current_book = Books.objects.get(id=book_id)
    current_book.authors.add(selected_author) 
    return redirect(f'/books/{book_id}')

def additionalBook(request):
    book_id = int(request.POST['available_books'])
    selected_book = Books.objects.get(id=book_id)
    author_id = int(request.POST['add_book'])
    current_author = Authors.objects.get(id=author_id)
    current_author.books.add(selected_book)
    return redirect(f'/authors/{author_id}')