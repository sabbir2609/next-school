from django.urls import path
from .views import (
    HomePageView,
    NoticeListView,
    NoticeDetailView,
    NoticeCreateView,
    NoticeUpdateView,
    NoticeDeleteView,
)

app_name = "homepage"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    # Notice URLs
    path("notices/", NoticeListView.as_view(), name="notice_list"),
    path("notices/<str:slug>/", NoticeDetailView.as_view(), name="notice_detail"),
    path("notices/create/", NoticeCreateView.as_view(), name="notice_create"),
    path(
        "notices/<str:slug>/update/", NoticeUpdateView.as_view(), name="notice_update"
    ),
    path(
        "notices/<str:slug>/delete/", NoticeDeleteView.as_view(), name="notice_delete"
    ),
]
