from django.urls import path
from .views import (
    HomePageView,
    # Notices
    NoticeListView,
    NoticeDetailView,
    # Governance Bodies
    GovernanceBodyDetailView,
)

app_name = "homepage"

# fmt: off

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),

    # Notice URLs
    path("notices/", NoticeListView.as_view(), name="notice_list"),
    path("notices/<str:slug>/", NoticeDetailView.as_view(), name="notice_detail"),

    # governing bodies URLs
    # path("governance_bodies/", GovernanceBodyListView.as_view(), name="governance_body_list"),
    path("governance_bodies/<str:slug>", GovernanceBodyDetailView.as_view(), name="governance_body_detail"),
]
