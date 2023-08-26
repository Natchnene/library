from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .models import Reader, User


class ReadersListView(ListView):
    model = Reader
    template_name = "list_readers.html"


class UserCreateView(CreateView):
    model = User
    fields = ["first_name", "middle_name", "last_name"]
    template_name = "create_user.html"
    success_url = "/list_readers.html"
