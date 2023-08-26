from django.urls import path

from .views import ReadersListView, UserCreateView

urlpatterns = [path("get_readers/", ReadersListView.as_view(), name="get_reader"), path("create_user/", UserCreateView.as_view(), name="create_user")]
