import datetime
from typing import Any, Dict, Optional

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.db import models
from django.forms import ValidationError, modelformset_factory
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from school.forms import AttendanceForm, StudentAssignForm, StudentForm

from .models import (Attendance, Class, Section, SectionSubject, Student,
                     StudentAssign, Subject, Teacher)

from dal import autocomplete


class HomeView(TemplateView):
    template_name = "school/home.html"


class StudentListView(ListView):
    model = Student
    context_object_name = "students"
    template_name = "school/student_list.html"
    paginate_by = 10
            

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


class StudentAssignView(SuccessMessageMixin, CreateView):
    template_name = "school/assign_student.html"
    form_class = StudentAssignForm

    def get_success_url(self):
        return reverse_lazy("school:section_detail", kwargs={"pk": self.object.section.id})

    def get_success_message(self, cleaned_data):
        return "Student assigned successfully"

# student autocomplete view
class StudentAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = StudentAssign.objects.all()
        if self.q:
            qs = qs.filter(student__name_en__istartswith=self.q)
        return qs

# Attendance Create for specific student
class StudentAttendanceCreateView(CreateView):
    template_name = "school/attendance/student_attendance_add.html"
    form_class = AttendanceForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student_id = self.kwargs["pk"]
        context["student"] = StudentAssign.objects.get(student__student_id=student_id)
        return context

    def form_valid(self, form):
        # Set the student field to the object with the URL parameter primary key
        student = StudentAssign.objects.get(student__student_id=self.kwargs["pk"])
        date = form.cleaned_data["date"]
        # Check if attendance already exists for this student on this date
        if Attendance.objects.filter(student_assign=student, date=date).exists():
            messages.warning(self.request, "Attendance already exists for this student on this date")
            return super().form_invalid(form)
        form.instance.student = student
        return super().form_valid(form)


    def get_success_url(self):
        return reverse_lazy("school:attendance_report_detail" , kwargs={"pk": self.kwargs["pk"]})


# Attendance Report for specific student
class StudentAttendanceReportDetailView(ListView):
    template_name = "school/attendance/student_attendance_report.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student_id = self.kwargs["pk"]
        
        try:
            StudentAssign.objects.filter(student_id=student_id) # TODO: wtf is this? 🙄
            context["student"] = StudentAssign.objects.get(student_id=student_id)
            context["attendance"] = Attendance.objects.filter(
                student__student__student_id=student_id
            )
            return context
        except StudentAssign.DoesNotExist:
            messages.warning(self.request, "No attendance record found. You must assign the student to a section first.")
            raise Http404("Student does not exist")
        
    def get(self, request, *args, **kwargs):
        if not self.get_queryset():
            messages.warning(request, "No attendance record found. Add attendance first.")
            return redirect("school:attendance_add", pk=kwargs["pk"])
        return super().get(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        student_id = self.kwargs["pk"]
        return Attendance.objects.filter(student__student__student_id=student_id)


# Attendance Update for any student
class AttendanceCreateView(CreateView):
    model = Attendance
    template_name = "school/attendance/attendance_create_any.html"
    form_class = AttendanceForm
    def get_success_url(self):
        return reverse_lazy("school:attendance_all_report")
    


#  Attendance Report for all students
class AttendanceReportView(ListView):
    # TODO: (44 queries including 40 similar and 20 duplicates) 🙄 check debug toolbar
    template_name = "school/attendance/attendance_report_all.html"
    model = Attendance
    context_object_name = "attendance_list"
    paginate_by = 10


