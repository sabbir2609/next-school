from pprint import pprint
from django.contrib import messages
from django.forms import ValidationError
from django.forms.utils import ErrorList
from django.db import IntegrityError, transaction
from django.db.models import Q
from django.db.models.deletion import ProtectedError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.utils.text import slugify
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import SingleObjectMixin
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    TemplateView,
    DetailView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    FormView,
)

from dal import autocomplete

from taggit.models import Tag

import logging

logger = logging.getLogger(__name__)

from school.models import (
    SectionSubject,
    Student,
    StudentAssign,
    Subject,
    Teacher,
    Class,
    Section,
)
from school.forms import StudentAssignForm, StudentForm, TeacherForm

from homepage.models import Notice
from homepage.views import NoticeListView, NoticeDetailView

from .forms import (
    NoticeForm,
    SectionForm,
    SectionUpdateForm,
    SectionSubjectFormset,
)


class DashboardView(TemplateView):
    template_name = "dashboard/dashboard.html"


# app: homepage views
class DashboardNoticeListView(NoticeListView):
    template_name = "dashboard/notice/notice_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag_list"] = set(
            Tag.objects.filter(notice__isnull=False)
        )  # there should be more efficient way
        return context


class NoticeTagAutoComplete(autocomplete.Select2QuerySetView):
    paginate_by = 10

    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #     return Tag.objects.none()

        qs = Tag.objects.filter(
            taggit_taggeditem_items__content_type=ContentType.objects.get_for_model(
                Notice
            )
        ).distinct()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
            print(qs)

        return qs

    def get_create_option(self, context, q):
        return []


class DashboardNoticeDetailView(NoticeDetailView):
    template_name = "dashboard/notice/notice_detail.html"


class NoticeCreateView(SuccessMessageMixin, CreateView):
    form_class = NoticeForm
    model = Notice
    template_name = "dashboard/notice/notice_create.html"

    def get_success_url(self):
        return reverse_lazy(
            "dashboard:notice_detail", kwargs={"slug": self.object.slug}
        )

    def form_valid(self, form):
        notice = form.save(commit=False)
        notice.slug = slugify(f"{notice.title} {notice.date}")

        try:
            notice.save()
        except IntegrityError as e:
            messages.error(
                self.request,
                "A notice with this title and date already exists! Change the title or contact the administrator.",
            )
            return self.form_invalid(form)

        messages.success(
            self.request,
            f"Notice <em class='text-black'> {form.cleaned_data['title']} </em> created successfully",
        )
        return super().form_valid(form)


class NoticeUpdateView(UpdateView):
    model = Notice
    template_name = "dashboard/notice/notice_update.html"
    form_class = NoticeForm

    def form_valid(self, form):
        if not form.has_changed():
            messages.warning(self.request, "Nothing to update")
            return super().form_invalid(form)

        messages.success(
            self.request,
            f"Notice <em class='text-black'> {form.cleaned_data['title']} </em> updated successfully",
        )
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "dashboard:notice_detail", kwargs={"slug": self.object.slug}
        )


class NoticeDeleteView(SuccessMessageMixin, DeleteView):
    model = Notice

    def get_success_url(self):
        return reverse_lazy("dashboard:notice_list")

    def get_success_message(self, cleaned_data):
        return "Notice deleted successfully"


#####################
# app: school views #
#####################


class StudentListView(ListView):
    model = Student
    context_object_name = "students"
    template_name = "dashboard/student/student_list.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("q")
        if search_query:
            queryset = queryset.filter(
                Q(name_en__icontains=search_query)
                | Q(student_id__icontains=search_query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        students = self.get_queryset()
        page = self.request.GET.get("page")
        paginator = Paginator(students, self.paginate_by)
        try:
            students = paginator.page(page)
        except PageNotAnInteger:
            students = paginator.page(1)
        except EmptyPage:
            students = paginator.page(paginator.num_pages)
        context["students"] = students
        return context


class StudentDetailView(DetailView):
    model = Student
    template_name = "dashboard/student/student_detail.html"


class StudentUpdateView(UpdateView):
    model = Student
    template_name = "dashboard/student/student_update.html"
    form_class = StudentForm

    def get_success_url(self):
        return reverse_lazy(
            "dashboard:student_detail", kwargs={"pk": self.kwargs["pk"]}
        )

    def form_valid(self, form):
        if not form.has_changed():
            messages.warning(self.request, "Nothing to update")
            return super().form_invalid(form)

        messages.success(
            self.request,
            f" '{form.cleaned_data['name_en']}' profile updated successfully",
        )
        return super().form_valid(form)


class StudentDeleteView(SuccessMessageMixin, DeleteView):
    model = Student
    success_url = reverse_lazy("dashboard:student_list")

    def get_success_message(self, cleaned_data):
        return "Student deleted successfully"


class StudentCreateView(SuccessMessageMixin, CreateView):
    model = Student
    template_name = "dashboard/student/student_add.html"
    fields = ["student_id", "name_en", "birth_certificate_no", "image"]

    def get_success_url(self):
        return reverse_lazy("dashboard:student_detail", kwargs={"pk": self.object.pk})

    def get_success_message(self, cleaned_data):
        return "Student profile created successfully"


class StudentAssignView(SuccessMessageMixin, CreateView):
    template_name = "dashboard/student/student_assign.html"
    form_class = StudentAssignForm

    def get_success_url(self):
        return reverse_lazy(
            "school:section_detail", kwargs={"pk": self.object.section.id}
        )

    def get_success_message(self, cleaned_data):
        return "Student assigned successfully"


###############
# class views #
###############


class ClassListView(ListView):
    model = Class
    context_object_name = "classes"
    template_name = "dashboard/class/class_list.html"


class ClassCreateView(SuccessMessageMixin, CreateView):
    model = Class
    fields = ["title", "teacher", "description"]
    template_name = "dashboard/class/class_add.html"

    def get_success_url(self):
        return reverse_lazy("dashboard:class_detail", kwargs={"slug": self.object.slug})

    def form_valid(self, form):
        title = form.save(commit=False)
        title.slug = slugify(title)

        try:
            title.save()
        except IntegrityError as e:
            messages.error(
                self.request,
                "A Class already exists! Change the title or contact the administrator.",
            )
            return self.form_invalid(form)

        messages.success(
            self.request,
            f"Notice <em class='text-black'> {form.cleaned_data['title']} </em> created successfully",
        )
        return super().form_valid(form)


class ClassDetailView(DetailView):
    model = Class
    template_name = "dashboard/class/class_detail.html"


class ClassUpdateView(SuccessMessageMixin, UpdateView):
    model = Class
    template_name = "dashboard/class/class_update.html"
    fields = ["title", "teacher", "description"]

    def get_success_url(self):
        return reverse_lazy("dashboard:class_detail", kwargs={"slug": self.object.slug})

    def form_valid(self, form):
        if not form.has_changed():
            messages.warning(self.request, "Nothing to update")
            return super().form_invalid(form)

        messages.success(
            self.request,
            f"<em class='text-black'> {form.cleaned_data['title']} </em> updated successfully",
        )
        return super().form_valid(form)


class ClassDeleteView(SuccessMessageMixin, DeleteView):
    model = Class
    template_name = "dashboard/class/class_confirm_delete.html"
    success_message = "Class deleted successfully"

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
            messages.success(self.request, self.get_success_message(form.cleaned_data))
            return response
        except ProtectedError as e:
            error_message = "Cannot delete the class due to related students. Please reassign or delete associated students before deleting this class."
            messages.error(self.request, error_message)
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy("dashboard:class_detail", kwargs={"slug": self.object.slug})


###############
# Teacher views #
###############


class TeacherListView(ListView):
    model = Teacher
    context_object_name = "teachers"
    template_name = "dashboard/teacher/teacher_list.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(TeacherListView, self).get_context_data(**kwargs)
        teachers = self.get_queryset()
        page = self.request.GET.get("page")
        paginator = Paginator(teachers, self.paginate_by)
        try:
            teachers = paginator.page(page)
        except PageNotAnInteger:
            teachers = paginator.page(1)
        except EmptyPage:
            teachers = paginator.page(paginator.num_pages)
        context["teachers"] = teachers
        return context


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = "dashboard/teacher/teacher_detail.html"


class TeacherUpdateView(SuccessMessageMixin, UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = "dashboard/teacher/teacher_update.html"

    def get_success_url(self):
        return reverse_lazy("dashboard:teacher_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        if not form.has_changed():
            messages.warning(self.request, "Nothing to update")
            return super().form_invalid(form)

        messages.success(
            self.request,
            f" '{form.cleaned_data['name_en']}' profile updated successfully",
        )
        return super().form_valid(form)


class TeacherDeleteView(SuccessMessageMixin, DeleteView):
    model = Teacher
    template_name = "dashboard/teacher/teacher_confirm_delete.html"
    success_url = reverse_lazy("dashboard:teacher_list")

    def get_success_message(self, cleaned_data):
        return "Teacher deleted successfully"


class TeacherCreateView(SuccessMessageMixin, CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = "dashboard/teacher/teacher_add.html"

    def get_success_url(self):
        return reverse_lazy("dashboard:teacher_detail", kwargs={"pk": self.object.pk})

    def get_success_message(self, cleaned_data):
        return "Teacher profile created successfully"


##################
# Subjects views #
##################


class SubjectListView(ListView):
    model = Subject
    context_object_name = "subjects"
    template_name = "dashboard/subject/subject_list.html"


class SubjectCreateView(SuccessMessageMixin, CreateView):
    model = Subject
    fields = "__all__"
    template_name = "dashboard/subject/subject_add.html"

    def get_success_url(self):
        return reverse_lazy("dashboard:subject_list")

    def get_success_message(self, cleaned_data):
        return "Subject created successfully"


#################
# Section views #
#################


class SectionListView(ListView):
    model = Section
    context_object_name = "sections"
    template_name = "dashboard/section/section_list.html"


class SectionDetailView(DetailView):
    model = Section
    template_name = "dashboard/section/section_detail.html"
    context_object_name = "section"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get all students of this section
        context["students"] = StudentAssign.objects.filter(
            section=self.object
        ).select_related("student")

        # total students of this section.
        context["total_students"] = context["students"].count()

        # get all subjects of this section
        context["subjects"] = SectionSubject.objects.filter(section_id=self.object.id)

        return context


class SectionCreateView(SuccessMessageMixin, CreateView):
    model = Section
    form_class = SectionForm
    template_name = "dashboard/section/section_add_or_update.html"

    def get_success_message(self, cleaned_data):
        return "Section created successfully"

    def get_success_url(self):
        return reverse_lazy("dashboard:section_detail", kwargs={"pk": self.object.pk})


class SectionUpdateView(UpdateView):
    model = Section
    form_class = SectionUpdateForm
    template_name = "dashboard/section/section_add_or_update.html"

    def form_valid(self, form):
        if not form.has_changed():
            messages.warning(self.request, "Nothing to update")
            return super().form_invalid(form)

    def get_success_message(self, cleaned_data):
        return "Section updated successfully"

    def get_success_url(self):
        return reverse_lazy("dashboard:section_detail", kwargs={"pk": self.object.pk})


class SectionSubjectEditView(SingleObjectMixin, FormView):
    model = Section
    template_name = "dashboard/section/section_subject_edit.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Section.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Section.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return SectionSubjectFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Section Subject change successfully")
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy("dashboard:section_detail", kwargs={"pk": self.object.pk})


class SectionDeleteView(SuccessMessageMixin, DeleteView):
    model = Section
    template_name = "dashboard/section/section_confirm_delete.html"
    success_url = reverse_lazy("dashboard:section_list")

    def get_success_message(self, cleaned_data):
        return "Section deleted successfully"


def delete_section_subject(request, section_subject_id):
    section_subject = get_object_or_404(SectionSubject, id=section_subject_id)
    section_id = section_subject.section.id
    section_subject.delete()
    messages.success(request, "Section Subject deleted successfully")
    return redirect("dashboard:section_edit", pk=section_id)
