from itertools import chain

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Book, IssueBook


class InLibraryBookListView(ListView):
    model = Book
    template_name = "list_books_in_library.html"

    def get_queryset(self):
        all_books = Book.objects.all()
        books_on_hand = IssueBook.objects.filter(book_return__isnull=True)
        books_in_library = all_books.exclude(id__in=books_on_hand.values("id"))
        return books_in_library


class OnHandBookListView(ListView):
    model = IssueBook
    template_name = "list_books_on_hand.html"
    queryset = IssueBook.objects.filter(book_return__isnull=True)


def get_book(request):
    date = request.POST.get("date")
    issue_book = IssueBook(book_get=date)
    issue_book.save()
    return HttpResponseRedirect(redirect_to="/book/")


def return_book(request):
    date = request.POST.get("date")
    issue_book = IssueBook(book_return=date)
    issue_book.save()
    return HttpResponseRedirect(redirect_to="/book/")
