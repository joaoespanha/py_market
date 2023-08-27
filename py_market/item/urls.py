from django.urls import path
from . import views


app_name = "item"

urlpatterns = [
    path("<int:id>", views.details, name="details"),
    path("new", views.new, name="new"),
    path("delete/<int:id>", views.delete, name="delete"),
    path("edit/<int:id>", views.edit, name="edit"),
]
