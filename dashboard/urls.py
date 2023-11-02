from django.urls import path
from .views import (
    DashboardView,
    NoticeTagAutoComplete,
    # notice views
    DashboardNoticeListView,
    DashboardNoticeDetailView,
    NoticeCreateView,
    NoticeDeleteView,
    NoticeUpdateView,
    # student views
    StudentCreateView,
    StudentDeleteView,
    StudentDetailView,
    StudentListView,
    StudentUpdateView,
    StudentAssignView,
    # class views
    ClassListView,
    ClassDetailView,
    ClassCreateView,
    ClassUpdateView,
    ClassDeleteView,
    # teacher views
    TeacherCreateView,
    TeacherListView,
    TeacherDetailView,
    TeacherUpdateView,
    TeacherDeleteView,
    # section views
    SectionListView,
    SectionDetailView,
    SectionCreateView,
    # subject views
    SubjectListView,
    SubjectCreateView,
    SectionUpdateView,
    delete_section_subject,
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
    path("dashboard/students/new/", StudentCreateView.as_view(), name="student_new"),
    path("dashboard/students/<int:pk>/update/", StudentUpdateView.as_view(), name="student_update"),
    path("dashboard/students/<int:pk>/delete/", StudentDeleteView.as_view(), name="student_delete"),
    # Student Assign URLs
    path("dashboard/students/assign/", StudentAssignView.as_view(), name="student_assign"),
    ################
    # Class URLs #
    ################
    path("dashboard/classes/", ClassListView.as_view(), name="class_list"),
    path("dashboard/classes/new/", ClassCreateView.as_view(), name="class_new"),
    path("dashboard/classes/<str:slug>/", ClassDetailView.as_view(), name="class_detail"),
    path("dashboard/classes/<str:slug>/update/", ClassUpdateView.as_view(), name="class_update"),
    path("dashboard/classes/<str:slug>/delete/", ClassDeleteView.as_view(), name="class_delete"),
    ################
    # Teacher URLs #
    ################
    path("dashboard/teachers/", TeacherListView.as_view(), name="teacher_list"),
    path("dashboard/teachers/new/", TeacherCreateView.as_view(), name="teacher_new"),
    path("dashboard/teachers/<int:pk>/", TeacherDetailView.as_view(), name="teacher_detail"),
    path("dashboard/teachers/<int:pk>/update/", TeacherUpdateView.as_view(), name="teacher_update"),
    path("dashboard/teachers/<int:pk>/delete/", TeacherDeleteView.as_view(), name="teacher_delete"),
    ################
    # Section URLs #
    ################
    path("dashboard/sections/", SectionListView.as_view(), name="section_list"),
    path("dashboard/sections/new/", SectionCreateView.as_view(), name="section_new"),
    path("dashboard/sections/<int:pk>/", SectionDetailView.as_view(), name="section_detail"),
    # delete section subjects
    path("dashboard/sections/subject/<int:pk>/delete", delete_section_subject, name="delete_section_subject"),
    ################
    # Subject URLs #
    ################
    path("dashboard/subjects/", SubjectListView.as_view(), name="subject_list"),
    path("dashboard/sections/<int:pk>/update/", SectionUpdateView.as_view(), name="section_update"),
    path("dashboard/subjects/new/", SubjectCreateView.as_view(), name="subject_new"),




]
