from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from homepage.forms import NoticeForm

from homepage.models import Notice
from homepage.views import NoticeListView, NoticeDetailView


class DashboardView(TemplateView):
    template_name = "dashboard/dashboard.html"


class DashboardNoticeListView(NoticeListView):
    template_name = "dashboard/notice/notice_list.html"


class DashboardNoticeDetailView(NoticeDetailView):
    template_name = "dashboard/notice/notice_detail.html"


class NoticeCreateView(CreateView):
    form_class = NoticeForm
    model = Notice
    template_name = "dashboard/notice/notice_create.html"

    def get_success_url(self):
        return reverse_lazy(
            "dashboard:notice_detail", kwargs={"slug": self.object.slug}
        )

    def get_success_message(self, cleaned_data):
        return "Notice created successfully"


class NoticeUpdateView(UpdateView):
    form_class = NoticeForm
    model = Notice
    template_name = "dashboard/notice/notice_update.html"

    def get_success_url(self):
        return reverse_lazy(
            "dashboard:notice_detail", kwargs={"slug": self.object.slug}
        )

    def get_success_message(self, cleaned_data):
        return "Notice updated successfully"


class NoticeDeleteView(DeleteView):
    model = Notice
    success_url = "/notices/"
