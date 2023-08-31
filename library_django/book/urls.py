from django.urls import path

from .views import (
    start_page_book,
    create_issue_book,
    in_library_book_list,
    form_for_create_issue_book,
    success,
    on_hand_book_list,
    form_for_update_issue_book,
    update_issue_book,

)

urlpatterns = [
    path("start_page_book/<int:id>", start_page_book, name="start_page_book"),
    path("list_books_in_library/reader/<int:reader_id>", in_library_book_list, name="list_books_in_library"),
    path("list_books_on_hand/reader/<int:reader_id>", on_hand_book_list, name="list_books_on_hand"),
    path("form_for_create_issue_book/reader/<int:reader_id>", form_for_create_issue_book, name="form_for_create_issue_book"),
    path("create_issue_book/reader/<int:reader_id>", create_issue_book, name="create_issue_book"),
    path("success/reader/<int:reader_id>", success, name="success"),
    path("form_for_update_issue_book/on_hand_book/<int:on_hand_book_id>", form_for_update_issue_book, name="form_for_update_issue_book"),
    path("update_issue_book/on_hand_book/<int:on_hand_book_id>", update_issue_book, name="update_issue_book"),
]
