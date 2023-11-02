from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from school.forms import (
    AttendanceForm,
    StudentAssignForm,
    StudentForm,
    StudentResultForm,
)
from dal import autocomplete

from .models import (
    Attendance,
    Section,
    SectionSubject,
    StudentAssign,
    Teacher,
    StudentResult,
)


# student autocomplete view for student assign
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
            messages.warning(
                self.request, "Attendance already exists for this student on this date"
            )
            return super().form_invalid(form)
        form.instance.student = student
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "school:attendance_report_detail", kwargs={"pk": self.kwargs["pk"]}
        )


# Attendance Report for specific student
class StudentAttendanceReportDetailView(ListView):
    template_name = "school/attendance/student_attendance_report.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student_id = self.kwargs["pk"]

        try:
            StudentAssign.objects.filter(student_id=student_id)  # TODO: wtf is this? 🙄
            context["student"] = StudentAssign.objects.get(student_id=student_id)
            context["attendance"] = Attendance.objects.filter(
                student__student__student_id=student_id
            )
            return context
        except StudentAssign.DoesNotExist:
            messages.warning(
                self.request,
                "No attendance record found. You must assign the student to a section first.",
            )
            raise Http404("Student does not exist")

    def get(self, request, *args, **kwargs):
        if not self.get_queryset():
            messages.warning(
                request, "No attendance record found. Add attendance first."
            )
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


# student autocomplete view for student assign
class StudentResultAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = StudentAssign.objects.all()
        if self.q:
            qs = qs.filter(student__admission_class=self.q)
        return qs


class StudentResultCreateView(CreateView):
    model = StudentResult
    template_name = "school/result/student_result_add.html"
    form_class = StudentResultForm


class StudentResultDetailView(ListView):
    model = StudentResult
    template_name = "school/result/student_result_detail.html"
    context_object_name = "result"

    def get_queryset(self, *args, **kwargs):
        student_id = self.kwargs["student_id"]
        class_slug = self.kwargs["class_slug"]
        exam_slug = self.kwargs["exam_slug"]

        print(student_id, class_slug, exam_slug)

        # TODO: Filter by all arguments
        qs = (
            StudentResult.objects.filter(student_assign__student__student_id=student_id)
            .filter(exam_assign__exam__slug=exam_slug)
            .filter(exam_assign__subject__section__class_name__slug=class_slug)
        )

        return qs

        # return get_list_or_404(
        #     StudentResult,
        #     Q(student_assign__student__student_id=student_id),
        #     Q(exam_assign__subject__section__class_name__slug=class_slug),
        #     Q(exam_assign__exam__slug=exam_slug),
        # )

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)

    #     # reformat the code if it works
    #     student_id = self.kwargs["student_id"]
    #     student_assign = StudentAssign.objects.get(student__student_id=student_id)
    #     student_name = student_assign.student.name_en
    #     context["student_name"] = student_name

    #     # pprint(exam_assign)
    #     return context
