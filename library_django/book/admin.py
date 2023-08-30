from django.contrib import admin

from .models import Author, Book, IssueBook, OnHandBook

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(IssueBook)
admin.site.register(OnHandBook)
