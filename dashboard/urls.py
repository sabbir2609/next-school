from django.urls import path
from .views import (
    DashboardView,
    DashboardNoticeListView,
    NoticeTagAutoComplete,
    DashboardNoticeDetailView,
    NoticeCreateView,
    NoticeDeleteView,
    NoticeUpdateView,
    StudentCreateView,
    StudentDeleteView,
    StudentDetailView,
    StudentListView,
    StudentUpdateView,
    StudentAssignView,
)

app_name = "dashboard"

# fmt: off
urlpatterns = [
    # notice tag autocomplete url
    path("dashboard/notices/tag-autocomplete/", NoticeTagAutoComplete.as_view(), name="notice_tag_autocomplete"),

    # dashboard
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    # Dash Notice
    path("dashboard/notices/create/", NoticeCreateView.as_view(), name="notice_create"),
    path("dashboard/notices/", DashboardNoticeListView.as_view(), name="notice_list"),
    path("dashboard/notices/<str:slug>/", DashboardNoticeDetailView.as_view(), name="notice_detail"),
    path("dashboard/notices/<str:slug>/update/", NoticeUpdateView.as_view(), name="notice_update"),
    path("dashboard/notices/<str:slug>/delete/", NoticeDeleteView.as_view(), name="notice_delete"),
    ################
    # Student URLs #
    ################
    path("dashboard/students/", StudentListView.as_view(), name="student_list"),
    path("dashboard/students/<int:pk>/", StudentDetailView.as_view(), name="student_detail"),
    path("students/<int:pk>/update/", StudentUpdateView.as_view(), name="student_update"),
    path("students/<int:pk>/delete/", StudentDeleteView.as_view(), name="student_delete"),
    path("students/new/", StudentCreateView.as_view(), name="student_new"),
    # Student Assign URLs
    path("students/assign/", StudentAssignView.as_view(), name="student_assign"),
]
