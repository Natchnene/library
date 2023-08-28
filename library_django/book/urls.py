from django.urls import path

from .views import (
    CreateIssueBook,
    DeleteIssueBook,
    InLibraryBookListView,
    OnHandBookListView,
    start_page,
)

urlpatterns = [
    path("start_page_book/", start_page, name="start_page_book"),
    path("list_books_in_library/", InLibraryBookListView.as_view(), name="list_books_in_library"),
    path("list_books_on_hand/", OnHandBookListView.as_view(), name="list_books_on_hand"),
    path("get_book/", CreateIssueBook.as_view(), name="get_book"),
    path("return_book/<pk>", DeleteIssueBook.as_view(), name="return_book"),
]
