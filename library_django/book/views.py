from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView

from .models import Book, IssueBook


def start_page(request):
    return render(request, "start_page.html")


class InLibraryBookListView(ListView):
    model = Book
    template_name = "list_books_in_library.html"

    def get_queryset(self):
        all_books = Book.objects.all()
        books_on_hand = IssueBook.objects.all()
        books_in_library = all_books.exclude(id__in=books_on_hand.values("book_id"))
        return books_in_library


class OnHandBookListView(ListView):
    model = IssueBook
    template_name = "list_books_on_hand.html"
    queryset = IssueBook.objects.filter(book_return__isnull=True)


class CreateIssueBook(CreateView):
    model = IssueBook
    fields = ["book_get", "book"]
    template_name = "get_book.html"
    success_url = "/book/list_books_in_library/"


class DeleteIssueBook(DeleteView):
    model = IssueBook
    template_name = "return_book.html"
    success_url = "/book/list_books_in_library/"
