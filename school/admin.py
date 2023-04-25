from django.contrib import admin
from django.utils.html import format_html


from .models import (
    Subject,
    Class,
    Section,
    Student,
    Teacher,
    SectionSubject,
    StudentAssign,
    Attendance,
)

# Register your models here.


class SectionSubjectInline(admin.TabularInline):
    model = SectionSubject
    extra = 0


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    def get_class_name(self, obj):
        return obj.title

    get_class_name.short_description = "Class Name"

    list_display = (
        "get_class_name",
        "class_teacher",
        "description",
    )


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "class_name",
        "class_teacher",
        "total_students",
        "description",
    )
    inlines = [SectionSubjectInline]


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
                    "phone",
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
                    "fathers_phone",
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
                    "mothers_phone",
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


@admin.register(StudentAssign)
class StudentAssignAdmin(admin.ModelAdmin):
    pass


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    pass
