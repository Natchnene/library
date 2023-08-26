from django.urls import path

from .views import InLibraryBookListView, OnHandBookListView, get_book, return_book

urlpatterns = [
    path("list_books_in_library/", InLibraryBookListView.as_view(), name="list_books_in_library"),
    path("list_books_on_hand/", OnHandBookListView.as_view(), name="list_books_on_hand"),
    path("get_book/", get_book, name="get_book"),
    path("return_book/", return_book, name="return_book"),
]
