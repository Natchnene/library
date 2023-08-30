from django.db import models
from django.utils.translation import gettext_lazy as _
from reader.mixins import DateTimeMixin
from django.urls import reverse


class Author(models.Model, DateTimeMixin):
    first_name = models.CharField(max_length=100, blank=False)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f"{self.pk} - {self.first_name} {self.middle_name} {self.last_name}"


class Book(models.Model, DateTimeMixin):
    id = models.PositiveSmallIntegerField(_("unique book number"), primary_key=True, blank=False)
    name = models.CharField(_("book title"), max_length=250, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    available = models.BooleanField("Книга доступна?", default=True)

    def __str__(self):
        return f"{self.id} {self.name}"


class OnHandBook(models.Model, DateTimeMixin):
    reader = models.ForeignKey("reader.Reader", on_delete=models.CASCADE)
    book = models.OneToOneField(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.id} {self.book.name}"


class IssueBook(models.Model, DateTimeMixin):
    book_get = models.DateField(_("Введите дату"), blank=True, null=True, help_text="в формате: год-месяц-день")
    book_return = models.DateField(blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey("reader.Reader", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.id} - {self.book.name} Дата выдачи: {self.book_get} Дата сдачи: {self.book_return} Читатель: {self.reader.last_name_id}"
