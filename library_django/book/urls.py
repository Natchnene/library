from django.urls import path, re_path

from .views import (
    UpdateIssueBook,
    # OnHandBookListView,
    OnHandBookCreate,
    OnHandBookDelete,
    start_page_book,
    # create_on_hand_book,
    create_issue_book,
    in_library_book_list,
    form_for_create_issue_book,
    success,
    on_hand_book_list,
)

urlpatterns = [
    path("start_page_book/<int:id>", start_page_book, name="start_page_book"),
    path("list_books_in_library/reader/<int:reader_id>", in_library_book_list, name="list_books_in_library"),
    path("list_books_on_hand/reader/<int:reader_id>", on_hand_book_list, name="list_books_on_hand"),
    path("form_for_create_issue_book/reader/<int:reader_id>", form_for_create_issue_book, name="form_for_create_issue_book"),
    path("create_issue_book/reader/<int:reader_id>", create_issue_book, name="create_issue_book"),
    path("create_book_on_hand/", OnHandBookCreate.as_view(), name="create_book_on_hand"),
    path("delete_book_on_hand/<pk>", OnHandBookDelete.as_view(), name="delete_book_on_hand"),
    path("update_issue_book/", UpdateIssueBook.as_view(), name="update_issue_book"),
    path("success/reader/<int:reader_id>", success, name="success"),
]
