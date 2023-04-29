import datetime
from typing import Any, Dict
from django.views.generic import TemplateView, ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from school.forms import StudentForm, AttendanceForm
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


class HomeView(TemplateView):
    template_name = "school/home.html"


class StudentListView(ListView):
    model = Student
    context_object_name = "students"
    template_name = "student_list.html"


class StudentDetailView(DetailView):
    model = Student
    template_name = "school/student_detail.html"


class StudentCreateView(SuccessMessageMixin, CreateView):
    model = Student
    template_name = "school/student_add.html"
    fields = ["student_id", "name_en", "birth_certificate_no", "image"]

    def get_success_url(self):
        pk = self.object.pk
        return reverse_lazy("school:student_detail", kwargs={"pk": pk})

    def get_success_message(self, cleaned_data):
        return "Student profile created successfully"


class StudentUpdateView(UpdateView):
    model = Student
    template_name = "school/student_update.html"
    form_class = StudentForm

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse_lazy("school:student_detail", kwargs={"pk": pk})

    def form_valid(self, form):
        if not form.has_changed():
            messages.warning(self.request, "Nothing to update")
            return super().form_invalid(form)
        else:
            messages.success(self.request, "Student profile updated successfully")
            return super().form_valid(form)


class StudentDeleteView(SuccessMessageMixin, DeleteView):
    model = Student
    template_name = "school/student_confirm_delete.html"
    success_url = reverse_lazy("school:student_list")

    def get_success_message(self, cleaned_data):
        return "Student deleted successfully"


class SectionListView(ListView):
    model = Section
    context_object_name = "sections"
    template_name = "school/section_list.html"


# TODO: TeacherListView - config urls and templates
class TeacherListView(ListView):
    model = Teacher
    context_object_name = "teachers"
    template_name = "school/teacher_list.html"
    pass


# TODO: TeacherDetailView urls and templates
class TeacherDetailView(DetailView):
    model = Teacher
    template_name = "school/teacher_detail.html"
    context_object_name = "teacher"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subjects"] = SectionSubject.objects.filter(
            teachers=self.object
        ).select_related("section", "subject")
        return context

    pass


class SectionDetailView(DetailView):
    model = Section
    template_name = "school/section_detail.html"
    context_object_name = "section"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get all students of this section
        context["students"] = StudentAssign.objects.filter(
            section=self.object
        ).select_related("student")

        # get total students of this section
        total_students = context["students"].count()
        context["total_students"] = total_students

        # get all subjects of this section
        context["subjects"] = SectionSubject.objects.filter(section_id=self.object.id)

        return context


class AttendanceView(CreateView):
    template_name = "school/attendance.html"
    form_class = AttendanceForm

    def get_success_url(self):
        return reverse_lazy("school:attendance")


# TODO: AttendanceView - config urls and templates
class AttendanceSectionListView(TemplateView):
    template_name = "school/attendance_by_section.html"
    model = Attendance
    context_object_name = "attendance_list"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
        context["attendance_list"] = Attendance.objects.all().filter(
            student__section_id=self.kwargs["pk"]
        )
        print(context["attendance_list"])
        return context
