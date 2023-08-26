from itertools import chain

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Book, IssueBook


class InLibraryBookListView(ListView):
    model = IssueBook
    template_name = "list_books_in_library.html"

    def get_queryset(self):
        books = IssueBook.objects.filter(book_return__isnull=False)
        all_books = Book.objects.all()
        books_issue = IssueBook.objects.all()
        books_new = all_books.exclude(id__in=books_issue.values("id"))
        queryset = chain(books, books_new)
        if isinstance(queryset, chain):
            return queryset


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
