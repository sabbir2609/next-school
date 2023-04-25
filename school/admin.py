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
    autocomplete_fields = [
        "teachers",
        "subject",
    ]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
    )

    search_fields = ("title",)


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
    search_fields = (
        "name",
        "class_name",
    )

    autocomplete_fields = [
        "class_teacher",
    ]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ["thumbnail"]

    def thumbnail(self, instance):
        if instance.image.name != "":
            return format_html(
                f'<img src="{instance.image.url}" height="100px" width="100px" />'
            )
        return ""

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
                    "date_of_birth",
                    "gender",
                    "religion",
                    "blood_group",
                    "student_id",
                    "birth_certificate_no",
                ]
            },
        ),
        (
            "Image",
            {
                "fields": [
                    ("image", "thumbnail"),
                ],
                # "classes": ["collapse"],
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

    search_fields = (
        "name_en",
        "student_id",
    )

    list_filter = (
        "admission_class",
        "status",
    )

    list_per_page = 10


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields = (
        "name_en",
        "teacher_id",
    )


@admin.register(StudentAssign)
class StudentAssignAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "section",
        "class_roll",
    )

    list_filter = (
        "section__name",
        "section__class_name",
    )

    autocomplete_fields = ["student", "section"]

    list_per_page = 10


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    pass
