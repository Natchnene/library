from django.db import models
from django.utils.translation import gettext_lazy as _
from reader.mixins import DateTimeMixin


class Author(models.Model, DateTimeMixin):
    first_name = models.CharField(max_length=100, blank=False)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f"{self.pk} - {self.first_name} {self.middle_name} {self.last_name}"


class Book(models.Model, DateTimeMixin):
    unique_number = models.CharField(_("unique book number"), max_length=250, blank=False, unique=True)
    name = models.CharField(_("book title"), max_length=250, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk} - {self.unique_number} {self.name}"


class IssueBook(models.Model, DateTimeMixin):
    book_get = models.DateField(blank=True, null=True)
    book_return = models.DateField(blank=True, null=True)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey("reader.Reader", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.pk} - {self.book} {self.reader}"
