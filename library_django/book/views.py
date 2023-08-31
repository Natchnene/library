from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Book, IssueBook, OnHandBook
from reader.models import Reader


def start_page_book(request, id):
    reader = {"data": Reader.objects.get(pk=id)}
    return render(request, "start_page_book.html", reader)


def in_library_book_list(request, reader_id):
    books = Book.objects.filter(available=True)
    reader = Reader.objects.get(pk=reader_id)
    context = {
        "books": books,
        "reader": reader
    }
    return render(request, "list_books_in_library.html", context)


def on_hand_book_list(request, reader_id):
    on_hand_book = OnHandBook.objects.filter(reader=reader_id).values("book__id", "book__name")
    on_hand_book_2 = OnHandBook.objects.filter(reader=reader_id)
    reader = Reader.objects.get(pk=reader_id)
    context = {
        "on_hand_book": on_hand_book,
        "on_hand_book_2": on_hand_book_2,
        "reader": reader
    }
    return render(request, "list_books_on_hand.html", context)


def form_for_create_issue_book(request, reader_id):
    reader = {"reader": Reader.objects.get(pk=reader_id)}
    return render(request, "form_for_create_issue_book.html", reader)


def create_issue_book(request, reader_id):
    date_get = request.POST.get("date")
    book_id = request.POST.get("book_id")
    book = Book.objects.get(pk=book_id)
    reader = Reader.objects.get(pk=reader_id)
    new_issue_book = IssueBook(book_get=date_get, book=book, reader=reader)
    new_issue_book.save()
    book.available = False
    book.save()
    new_on_hand_book = OnHandBook(book=book, reader=reader, issuebook=new_issue_book)
    new_on_hand_book.save()
    return HttpResponseRedirect(redirect_to=f"/book/success/reader/{reader.id}")


def success(request, reader_id):
    reader = {"reader": Reader.objects.get(pk=reader_id)}
    return render(request, "success.html", reader)


def form_for_update_issue_book(request, on_hand_book_id):
    on_hand_book = {"on_hand_book": OnHandBook.objects.get(pk=on_hand_book_id)}
    return render(request, "form_for_update_issue_book.html", on_hand_book)


def update_issue_book(request, on_hand_book_id):
    date_return = request.POST.get("date")
    book_id = request.POST.get("book_id")
    book = Book.objects.get(pk=book_id)
    book.available = True
    book.save()
    IssueBook.objects.filter(onhandbook=on_hand_book_id).update(book_return=date_return)
    on_hand_book = OnHandBook.objects.get(pk=on_hand_book_id)
    reader = Reader.objects.get(pk=on_hand_book.reader.id)
    on_hand_book.delete()
    return HttpResponseRedirect(redirect_to=f"/book/success/reader/{reader.id}")
