from django.contrib import admin
from django.urls import path

from tests import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("foo/", views.MyView.as_view(), name="class-view"),
    path("bar/", views.MyAPIView.as_view(), name="api-view"),
    path("spam/", views.MyAPIView, name="missing-as-view"),
    path("", views.my_view, name="function-view"),
]
