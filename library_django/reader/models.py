from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager
from .mixins import DateTimeMixin


class User(AbstractBaseUser, PermissionsMixin, DateTimeMixin):
    first_name = models.CharField(_("first name"), max_length=150, blank=False)
    middle_name = models.CharField(_("middle name"), max_length=150, blank=False)
    last_name_number = models.CharField(_("last name - unique number"), max_length=250, blank=False, unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_("Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."),
    )

    USERNAME_FIELD = "last_name_number"
    REQUIRED_FIELDS = ["first_name", "middle_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


class Reader(models.Model, DateTimeMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk} - {self.user.last_name_number} {self.user.first_name} {self.user.middle_name}"
