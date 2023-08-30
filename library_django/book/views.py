from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, BaseCreateView

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
    on_hand_books = OnHandBook.objects.filter(reader=reader_id).values("book__id", "book__name")
    reader = Reader.objects.get(pk=reader_id)
    context = {
        "on_hand_books": on_hand_books,
        "reader": reader
    }
    return render(request, "list_books_on_hand.html", context)


# class OnHandBookListView(ListView):
#     model = OnHandBook
#     template_name = "list_books_on_hand.html"
#
#     def get_queryset(self):
#         reader_id = self.kwargs["id"]
#         return OnHandBook.objects.filter(reader=reader_id)


class OnHandBookCreate(CreateView):
    model = OnHandBook
    fields = ["reader", "book"]
    template_name = "create_book_on_hand.html"
    success_url = "/book/create_issue_book/"


class OnHandBookDelete(DeleteView):
    model = OnHandBook
    template_name = "delete_book_on_hand.html"
    success_url = "/book/list_books_on_hand/"

    def get_queryset(self):
        reader_id = self.kwargs["id"]
        return OnHandBook.objects.filter(reader=reader_id)


# class CreateIssueBook(CreateView):
#     model = IssueBook
#     fields = ["book_get", "book__name", "book"]
#     template_name = "form_for_create_issue_book.html"


def form_for_create_issue_book(request, reader_id):
    reader = {"reader": Reader.objects.get(pk=reader_id)}
    return render(request, "form_for_create_issue_book.html", reader)


def create_issue_book(request, reader_id):
    data_get = request.POST.get("date")
    book_id = request.POST.get("book_id")
    book = Book.objects.get(pk=book_id)
    reader = Reader.objects.get(pk=reader_id)
    new_issue_book = IssueBook(book_get=data_get, book=book, reader=reader)
    new_issue_book.save()
    book.available = False
    book.save()
    new_on_hand_book = OnHandBook(book=book, reader=reader)
    new_on_hand_book.save()
    return HttpResponseRedirect(redirect_to=f"/book/success/reader/{reader.id}")


class UpdateIssueBook(UpdateView):
    model = IssueBook
    fields = ["book_return", "book.id"]
    template_name = "update_issue_book.html"


# def create_on_hand_book(request, id_reader, id_book):
#     context = {"reader": Reader.objects.get(pk=id_reader), "book": Book.objects.get(pk=id_book)}
#     return render(request, "start_page_book.html", context)


def success(request, reader_id):
    reader = {"reader": Reader.objects.get(pk=reader_id)}
    return render(request, "success.html", reader)
