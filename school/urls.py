from django.urls import path, include

from .views import (
    HomeView,
    # Student
    StudentListView,
    StudentDetailView,
    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,
    # Section
    SectionListView,
    SectionDetailView,
    # Attendance
    AttendanceView,
)


app_name = "school"


urlpatterns = [
    path("", HomeView.as_view(), name="hello"),
    # Student URLs
    path("students/", StudentListView.as_view(), name="student_list"),
    path("students/<int:pk>/", StudentDetailView.as_view(), name="student_detail"),
    path("students/new/", StudentCreateView.as_view(), name="student_new"),
    path("students/<int:pk>/edit/", StudentUpdateView.as_view(), name="student_edit"),
    path(
        "students/<int:pk>/delete/", StudentDeleteView.as_view(), name="student_delete"
    ),
    # Teacher URLs
    # path("teachers/", TeacherListView.as_view(), name="teacher_list"),
    # path("teachers/<int:pk>/", TeacherDetailView.as_view(), name="teacher_detail"),
    # path("teachers/new/", TeacherCreateView.as_view(), name="teacher_new"),
    # path("teachers/<int:pk>/edit/", TeacherUpdateView.as_view(), name="teacher_edit"),
    # path(
    #     "teachers/<int:pk>/delete/", TeacherDeleteView.as_view(), name="teacher_delete"
    # ),
    # Section URLs
    path("sections/", SectionListView.as_view(), name="section_list"),
    path("sections/<int:pk>/", SectionDetailView.as_view(), name="section_detail"),
    # Attendance URLs
    path("attendance/", AttendanceView.as_view(), name="attendance"),
]
