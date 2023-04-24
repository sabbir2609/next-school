from django.contrib import admin
from .models import (
    Class,
    Section,
    Parent,
    Student,
    Teacher,
    Subject,
    TeacherAssign,
    StudentAssign,
    Attendance,
    Exam,
    ExamAssign,
    ExamResult,
)


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "class_name"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "parent", "section"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["name", "section", "description"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(TeacherAssign)
class TeacherAssignAdmin(admin.ModelAdmin):
    list_display = [
        "teacher",
    ]
    list_filter = ["teacher"]
    search_fields = ["teacher"]


@admin.register(StudentAssign)
class StudentAssignAdmin(admin.ModelAdmin):
    list_display = ["student", "section"]
    list_filter = ["student"]
    search_fields = ["student"]


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ["student", "date", "status"]
    list_filter = ["student"]
    search_fields = ["student"]


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "date"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(ExamAssign)
class ExamAssignAdmin(admin.ModelAdmin):
    list_display = ["exam", "subject", "section", "is_done"]
    list_filter = ["exam", "is_done"]
    search_fields = ["exam"]
    list_editable = ["is_done"]


@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ["exam", "subject", "student", "marks"]
    list_filter = ["exam"]
    search_fields = ["exam"]
