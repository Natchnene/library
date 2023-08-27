from django.urls import path

from .views import UserCreateView, UsersListView

urlpatterns = [path("get_readers/", UsersListView.as_view(), name="get_reader"), path("create_user/", UserCreateView.as_view(), name="create_user")]
