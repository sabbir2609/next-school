from django.urls import include, path

from .views import (
    AttendanceCreateView,
    AttendanceReportView,
    StudentAttendanceCreateView,
    StudentAttendanceReportDetailView,
    StudentResultAutocompleteView,
    StudentAutocompleteView,
    StudentResultCreateView,
    StudentResultDetailView,
)

app_name = "school"


# fmt: off
urlpatterns = [

    # Student Autocomplete URLs for assigned students
    path("student-autocomplete/", StudentAutocompleteView.as_view(), name="student-autocomplete"),
    # Attendance URLs (Student)
    path("students/<int:pk>/attendance-add/", StudentAttendanceCreateView.as_view(), name="attendance_add"),
    path("students/<int:pk>/attendance-report/", StudentAttendanceReportDetailView.as_view(), name="attendance_report_detail"),
    # Attendance URLs (All)
    path("attendance/add/", AttendanceCreateView.as_view(), name="attendance_add_any"),
    path("attendance/all/", AttendanceReportView.as_view(), name="attendance_all_report"),
    # Result URLs
    path("student-result-autocomplete/", StudentResultAutocompleteView.as_view(), name="student-result-autocomplete"),
    path("students/result-add/", StudentResultCreateView.as_view(), name="result_add"),
    # Result Report URLs
    # students/student_id/class_name/exam_name/result-report/
    path(
        "students/<int:student_id>/<str:class_slug>/<str:exam_slug>/result-report/",
        StudentResultDetailView.as_view(),
        name="result_report_detail",
        ),
]
