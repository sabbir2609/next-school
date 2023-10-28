from django.contrib import messages
from django.db import IntegrityError
from django.utils.text import slugify
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from .forms import NoticeForm

from homepage.models import Notice
from homepage.views import NoticeListView, NoticeDetailView

from dal import autocomplete

from taggit.models import Tag

from django.contrib.contenttypes.models import ContentType


class DashboardView(TemplateView):
    template_name = "dashboard/dashboard.html"


class DashboardNoticeListView(NoticeListView):
    template_name = "dashboard/notice/notice_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag_list"] = set(Tag.objects.filter(notice__isnull=False))  # there should be more efficient way 
        return context



# TODO : Fix the tag query  and add tags from form

class NoticeTagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Tag.objects.none()
        
        qs = Tag.objects.all()

        print(qs.query)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs

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

        messages.success(self.request, f"Notice <em class='text-black'> {form.cleaned_data["title"]} </em> created successfully")
        return super().form_valid(form)


class NoticeUpdateView(UpdateView):
    model = Notice
    template_name = "dashboard/notice/notice_update.html"
    form_class = NoticeForm

    def form_valid(self, form):
        if not form.has_changed():
            messages.warning(self.request, "Nothing to update")
            return super().form_invalid(form)

        messages.success(self.request, f"Notice <em class='text-black'> {form.cleaned_data["title"]} </em> updated successfully")
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
