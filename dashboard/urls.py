from django.urls import path
from .views import (
    DashboardView,
    DashboardNoticeListView,
    NoticeTagAutocomplete,
    DashboardNoticeDetailView,
    NoticeCreateView,
    NoticeDeleteView,
    NoticeUpdateView,
)

app_name = "dashboard"

# fmt: off
urlpatterns = [
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    # Dash Notice
    path("dashboard/notices/create/", NoticeCreateView.as_view(), name="notice_create"),
    path("dashboard/notices/", DashboardNoticeListView.as_view(), name="notice_list"),
    path("dashboard/notices/<str:slug>/", DashboardNoticeDetailView.as_view(), name="notice_detail"),
    path("dashboard/notices/<str:slug>/update/", NoticeUpdateView.as_view(), name="notice_update"),
    path("dashboard/notices/<str:slug>/delete/", NoticeDeleteView.as_view(), name="notice_delete"),
    # notice tag autocomplete url
    path("dashboard/notices/tag-autocomplete/", NoticeTagAutocomplete.as_view(), name="notice_tag_autocomplete"),
]
