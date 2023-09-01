from django.urls import include, path

from .views import (
    AttendanceCreateView,
    AttendanceReportView,
    HomeView,
    SectionDetailView,
    SectionListView,
    StudentAssignView,
    StudentAttendanceCreateView,
    StudentAttendanceReportDetailView,
    StudentCreateView,
    StudentDeleteView,
    StudentDetailView,
    StudentListView,
    StudentResultAutocompleteView,
    StudentUpdateView,
    StudentAutocompleteView,
    StudentResultCreateView,
    StudentResultDetailView,
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
    # Assign Student URLs
    path("students/assign/", StudentAssignView.as_view(), name="student_assign"),
    # Student Autocomplete URLs for assigned students
    path(
        "student-autocomplete/",
        StudentAutocompleteView.as_view(),
        name="student-autocomplete",
    ),
    # Attendance URLs (Student)
    path(
        "students/<int:pk>/attendance-add/",
        StudentAttendanceCreateView.as_view(),
        name="attendance_add",
    ),
    path(
        "students/<int:pk>/attendance-report/",
        StudentAttendanceReportDetailView.as_view(),
        name="attendance_report_detail",
    ),
    # Attendance URLs (All)
    path("attendance/add/", AttendanceCreateView.as_view(), name="attendance_add_any"),
    path(
        "attendance/all/", AttendanceReportView.as_view(), name="attendance_all_report"
    ),
    # Section URLs
    path("sections/", SectionListView.as_view(), name="section_list"),
    path("sections/<int:pk>/", SectionDetailView.as_view(), name="section_detail"),
    # Result URLs
    path(
        "student-result-autocomplete/",
        StudentResultAutocompleteView.as_view(),
        name="student-result-autocomplete",
    ),
    path("students/result-add/", StudentResultCreateView.as_view(), name="result_add"),
    # Result Report URLs
    # students/student_id/class_name/exam_name/result-report/
    path(
        "students/<int:student_id>/<str:class_slug>/<str:exam_slug>/result-report/",
        StudentResultDetailView.as_view(),
        name="result_report_detail",
    ),
]
