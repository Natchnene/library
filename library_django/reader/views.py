from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .models import Reader


class UsersListView(ListView):
    model = Reader
    template_name = "list_readers.html"


class UserCreateView(CreateView):
    model = Reader
    fields = ["last_name_id", "first_name", "middle_name"]
    template_name = "create_user.html"
    success_url = "/reader/get_readers/"
