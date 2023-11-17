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
    GuardianAddView,
    GuardianUpdateView,
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
    SectionDeleteView,
    # subject views
    SubjectListView,
    SubjectCreateView,
    SectionUpdateView,
    SectionSubjectEditView,
    # attendance views
    AttendanceIndexView,
    SectionStudentAttendanceCreateView,
    StudentAttendanceDetailView,
    SectionAttendanceCreateView,
    SectionAttendanceReportView,
    SectionAttendanceDetailView,
    StudentAttendanceReportView,
    # exam views
    ExamListView,
    ExamCreateView,
    ExamDeleteView,
    # exam assign
    ExamAssignCreateView,
    ExamSectionListView,
    ExamSectionSubjectListView,
    ExamSectionSubjectDetailView,
    ExamSectionSubjectUpdateView,
    # exam subject autocomplete
    ExamSubjectAutoComplete,
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
    # guardian URLs
    path("dashboard/student/<int:pk>/add_guardian", GuardianAddView.as_view(), name="guardian_add"),
    path("dashboard/student/<int:pk>/update_guardian", GuardianUpdateView.as_view(), name="guardian_update"),
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
    path("dashboard/sections/<int:pk>/subject/edit", SectionSubjectEditView.as_view(), name="section_subject_edit"),
    path("dashboard/sections/<int:pk>/update/", SectionUpdateView.as_view(), name="section_update"),
    path("dashboard/sections/<int:pk>/delete/", SectionDeleteView.as_view(), name="section_delete"),
    ################
    # Subject URLs #
    ################
    path("dashboard/subjects/", SubjectListView.as_view(), name="subject_list"),
    path("dashboard/sections/<int:pk>/update/", SectionUpdateView.as_view(), name="section_update"),
    path("dashboard/subjects/new/", SubjectCreateView.as_view(), name="subject_new"),
    ###################
    # Attendance URLs #
    ###################
    path("dashboard/attendance/", AttendanceIndexView.as_view(), name="attendance_index"),

    path("dashboard/students/attendance/add/", SectionStudentAttendanceCreateView.as_view(), name="section_student_attendance_new"),

    path("dashboard/students/attendance/<int:pk>/detail/", StudentAttendanceDetailView.as_view(), name="student_attendance_detail"),

    path("dashboard/sections/attendance/<int:pk>/detail/", SectionAttendanceDetailView.as_view(), name="section_attendance_detail"),

    path("dashboard/sections/attendance/<int:pk>/add/", SectionAttendanceCreateView.as_view(), name="section_attendance_add"),
    
    path("dashboard/sections/attendance/report/", SectionAttendanceReportView.as_view(), name="section_attendance_report"),

    path("dashboard/students/attendance/<str:pk>/report/", StudentAttendanceReportView.as_view(), name="student_attendance_report"),

    #############
    # exam urls #
    #############

    path("dashboard/exams/", ExamListView.as_view(), name="exam_list"),
    path("dashboard/exams/new/", ExamCreateView.as_view(), name="exam_new"),
    path("dashboard/exams/<str:slug>/delete/", ExamDeleteView.as_view(), name="exam_delete"),
    path("dashboard/exams/assign/", ExamAssignCreateView.as_view(), name="exam_assign"),
    path("dashboard/exams/<str:slug>/sections/", ExamSectionListView.as_view(), name="exam_section_list"),

    path("dashboard/exams/<str:slug>/sections/<int:section_id>/subjects/", ExamSectionSubjectListView.as_view(), name="exam_section_subject_list"),

    path("dashboard/exams/<str:slug>/sections/<int:section_id>/subjects/<int:pk>/details", ExamSectionSubjectDetailView.as_view(), name="exam_section_subject_detail"),

    path("dashboard/exams/<str:slug>/sections/<int:section_id>/subjects/<int:pk>/update", ExamSectionSubjectUpdateView.as_view(), name="exam_section_subject_update"),
    # exam subject autocomplete
    path("dashboard/exams/subject-autocomplete/", ExamSubjectAutoComplete.as_view(), name="exam_subject_autocomplete"),

]
