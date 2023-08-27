from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .models import Reader, User


class UsersListView(ListView):
    model = User
    template_name = "list_readers.html"


class UserCreateView(CreateView):
    model = User
    fields = ["first_name", "middle_name", "last_name_number"]
    template_name = "create_user.html"
    success_url = "/reader/get_readers/"
