from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student


class HomeView(TemplateView):
    template_name = "school/home.html"


class StudentListView(ListView):
    model = Student
    context_object_name = "students"
    template_name = "student_list.html"


class StudentDetailView(DetailView):
    model = Student
    template_name = "school/student_detail.html"


class StudentCreateView(CreateView):
    model = Student
    template_name = "school/student_add.html"
    fields = ["id", "name", "parent", "section"]
    success_url = reverse_lazy("school:student_list")


class StudentUpdateView(UpdateView):
    model = Student
    template_name = "school/student_update.html"
    fields = ["name", "parent", "section"]
    success_url = reverse_lazy("school:student_list")


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "school/student_confirm_delete.html"
    success_url = reverse_lazy("school:student_list")
