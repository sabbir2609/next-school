from django.contrib import admin
from django.utils.html import format_html


from .models import (
    Class,
    Section,
    Student,
    Teacher,
    Subject,
    TeacherAssign,
    StudentAssign,
    Attendance,
    Exam,
    ExamAssign,
    ExamAttendance,
    ExamResult,
)

# Register your models here.


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    def get_class_name(self, obj):
        return obj.title

    get_class_name.short_description = "Class Name"

    list_display = ("get_class_name", "class_teacher")


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "name_en",
        "student_id",
        "admission_class",
        "admission_date",
        "status",
    )
    fieldsets = [
        (
            "Personal Information",
            {
                "fields": [
                    (
                        "name_en",
                        "name_bn",
                    ),
                    "dob",
                    "gender",
                    "religion",
                    "blood_group",
                    "student_id",
                    "birth_certificate_no",
                    "image",
                ]
            },
        ),
        (
            "Contact Information",
            {
                "fields": [
                    "mobile_no",
                    "email",
                    "present_address",
                    "permanent_address",
                    "nationality",
                ]
            },
        ),
        (
            "Father's Information",
            {
                "fields": [
                    (
                        "fathers_name_en",
                        "fathers_name_bn",
                    ),
                    "fathers_occupation",
                    "fathers_nid",
                    "fathers_mobile_no",
                ]
            },
        ),
        (
            "Mother's Information",
            {
                "fields": [
                    (
                        "mothers_name_en",
                        "mothers_name_bn",
                    ),
                    "mothers_occupation",
                    "mothers_nid",
                    "mothers_mobile_no",
                ]
            },
        ),
        (
            "Other Information",
            {
                "fields": [
                    "admission_date",
                    "admission_class",
                    "comment",
                    "status",
                ]
            },
        ),
    ]
    search_fields = ("name_en", "student_id", "admission_class__title")
    list_filter = ("admission_class", "status")


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(TeacherAssign)
class TeacherAssignAdmin(admin.ModelAdmin):
    pass


@admin.register(StudentAssign)
class StudentAssignAdmin(admin.ModelAdmin):
    pass


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    pass


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    pass


@admin.register(ExamAssign)
class ExamAssignAdmin(admin.ModelAdmin):
    pass


@admin.register(ExamAttendance)
class ExamAttendanceAdmin(admin.ModelAdmin):
    pass


@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    pass
