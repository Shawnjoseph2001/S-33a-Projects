from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.page, name="page"),
    path("search", views.search, name="search")
]
