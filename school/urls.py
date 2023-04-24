from django.urls import path, include

from .views import (
    HomeView,
    StudentListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
)


app_name = "school"


urlpatterns = [
    path("", HomeView.as_view(), name="hello"),
    path("students/", StudentListView.as_view(), name="student_list"),
    path("students/<int:pk>/", StudentDetailView.as_view(), name="student_detail"),
    path("students/new/", StudentCreateView.as_view(), name="student_new"),
    path("students/<int:pk>/edit/", StudentUpdateView.as_view(), name="student_edit"),
    path(
        "students/<int:pk>/delete/", StudentDeleteView.as_view(), name="student_delete"
    ),
]
