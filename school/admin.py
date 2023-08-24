from django.contrib import admin
from django.utils.html import format_html
from django.contrib.admin import DateFieldListFilter

from .models import (Attendance, Class, Exam, ExamAssign, Section,
                     SectionSubject, Student, StudentAssign, Subject, Teacher, Result)

# Register your models here.


class SectionSubjectInline(admin.TabularInline):
    model = SectionSubject
    extra = 0
    autocomplete_fields = [
        # "teachers",
        # "subject",
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
        "section_teacher",
        "seat",
        "description",
    )
    inlines = [SectionSubjectInline]
    search_fields = (
        "name",
        "class_name",
    )

    autocomplete_fields = [
        "section_teacher",
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
    list_display = (
        "name_en",
        "teacher_id",
        "phone",
    )
    search_fields = (
        "name_en",
        "teacher_id",
    )
    list_filter = ("gender",)
    list_per_page = 10


# student assign to section and class_roll admin
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

    autocomplete_fields = [
        "student",
        "section",
    ]

    search_fields = (
        "student__name_en",
        "student__student_id",
    )

    ordering = ("section__class_name", "section__name", "class_roll")
    list_per_page = 10


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):

    def get_student_id(self, obj):
        return obj.student_assign.student.student_id

    list_display = (
        "student_assign",
        "get_student_id",
        "date",
        "status",
    )

    search_fields = (
        "student_assign__student__student_id",
    )

    list_filter = (
        "student_assign__section__class_name",
        "student_assign__section__name",
        "status",
    )

    date_hierarchy = "date"

    list_per_page = 10

admin.site.register(Exam)
admin.site.register(ExamAssign)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):

    def get_student_id(self, obj):
        return obj.student_assign.student.student_id
    
    def get_exam_title(self, obj):
        return obj.exam_assign.exam.exam_title
    
    def get_subject_title(self, obj):
        return obj.exam_assign.subject.subject.title

    list_display = (
        "student_assign",
        "get_student_id",
        "get_exam_title",
        "get_subject_title",
    )

    # search_fields = (
    #     "student__student_id",
    #     "exam__title",
    #     "subject__title",
    # )

    # list_filter = (
    #     "student__admission_class",
    #     "exam__title",
    #     "subject__title",
    # )

    list_per_page = 10