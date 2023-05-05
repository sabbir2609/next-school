from django.urls import include, path

from .views import (  # Student; Assign Student; Section; Attendance
    AttendanceCreateViewView, AttendanceReportDetailView, AttendanceReportView,
    HomeView, SectionDetailView, SectionListView, StudentAssignView,
    StudentCreateView, StudentDeleteView, StudentDetailView, StudentListView,
    StudentUpdateView)

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
    # Assign Student URLs
    path("students/assign/", StudentAssignView.as_view(), name="student_assign"),

    # Attendance URLs
    path("students/<int:pk>/attendance-add/", AttendanceCreateViewView.as_view(), name="attendance_add"),
    path("students/<int:pk>/attendance-report/", AttendanceReportDetailView.as_view(), name="attendance_report_detail"),
    
    path("attendance/all", AttendanceReportView.as_view(), name="attendance_all_report"),

    # Section URLs
    path("sections/", SectionListView.as_view(), name="section_list"),
    path("sections/<int:pk>/", SectionDetailView.as_view(), name="section_detail"),

]
