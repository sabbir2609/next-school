from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from school.forms import StudentForm
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


class SectionDetailView(DetailView):
    model = Section
    template_name = "school/section_detail.html"
    context_object_name = "section"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        section = self.get_object()
        context["students"] = StudentAssign.objects.filter(section=section)
        return context
