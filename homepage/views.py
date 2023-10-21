from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import (
    DropdownNavigation,
    HistoryAndMission,
    Notice,
    GovernanceBody,
    Contact,
    UsefulLink,
    ImageGallery,
    Stat,
    WhatsHappening,
    CoCurricular,
    BrightStudent,
    BannerImage,
)

from .forms import NoticeForm


class HomePageView(TemplateView):
    template_name = "home/homepage.html"  # Adjust the template path as needed

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch data from your models and pass it to the template
        context["dropdowns"] = DropdownNavigation.objects.all()
        context["banner_images"] = BannerImage.objects.all()
        context["history_and_mission"] = HistoryAndMission.objects.all()
        context["notices"] = Notice.objects.all()[:20]
        context["important"] = Notice.objects.filter(tags__name__in=["important"])
        context["governance_bodies"] = GovernanceBody.objects.all()
        context["contacts"] = Contact.objects.all()
        context["useful_links"] = UsefulLink.objects.all()
        context["gallery_images"] = ImageGallery.objects.order_by("id")[
            :10
        ]  # will show recent 10 items
        context["stats"] = Stat.objects.all()
        context["whats_happening"] = WhatsHappening.objects.order_by("-date")[
            :4
        ]  # will show recent 4 items
        context["co_curricular"] = CoCurricular.objects.all()

        context["bright_students"] = BrightStudent.objects.all()

        return context


# ================= Notice CRUD ====================== #


class NoticeListView(ListView):
    model = Notice
    context_object_name = "notices"
    paginate_by = 15
    template_name = "home/notices/notice_list.html"

    def get_queryset(self):
        filter_value = self.request.GET.get("filter")
        if filter_value:
            return Notice.objects.filter(tags__name__in=[filter_value])
        return Notice.objects.all()

    def get_context_data(self, **kwargs):
        context = super(NoticeListView, self).get_context_data(**kwargs)
        notices = self.get_queryset()
        page = self.request.GET.get("page")
        paginator = Paginator(notices, self.paginate_by)
        try:
            notices = paginator.page(page)
        except PageNotAnInteger:
            notices = paginator.page(1)
        except EmptyPage:
            notices = paginator.page(paginator.num_pages)
        context["notices"] = notices
        return context


class NoticeDetailView(DetailView):
    model = Notice
    context_object_name = "notice"
    template_name = "home/notices/notice_detail.html"


class NoticeCreateView(CreateView):
    model = Notice
    fields = ["title", "slug", "description", "attachment"]
    template_name = "home/notices/notice_create.html"


class NoticeUpdateView(UpdateView):
    form_class = NoticeForm
    model = Notice
    template_name = "home/notices/notice_update.html"

    def get_success_url(self):
        return reverse_lazy("homepage:notice_detail", kwargs={"slug": self.object.slug})

    def get_success_message(self, cleaned_data):
        return "Notice updated successfully"


class NoticeDeleteView(DeleteView):
    model = Notice
    success_url = "/notices/"


# ================= Notice CRUD Ends ====================== #


class GovernanceBodyDetailView(DetailView):
    model = GovernanceBody
    context_object_name = "governance_body"
    template_name = "home/governance_body/governance_body_detail.html"
