from django.db import models
from django.utils.translation import gettext_lazy as _

from .mixins import DateTimeMixin


class Reader(models.Model, DateTimeMixin):
    last_name_id = models.CharField(_("Фамилия-уникальный номер читателя"), max_length=150, blank=False, unique=True)
    first_name = models.CharField(_("Имя"), max_length=150, blank=False)
    middle_name = models.CharField(_("Отчество"), max_length=150, blank=False)

    def __str__(self):
        return f"{self.pk} - {self.last_name_id} {self.first_name} {self.middle_name}"
