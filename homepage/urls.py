from django.urls import path
from .views import HomePageView, NoticeListView, NoticeDetailView

app_name = "homepage"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    # Notice URLs
    path("notices/", NoticeListView.as_view(), name="notice_list"),
    path("notices/<str:slug>/", NoticeDetailView.as_view(), name="notice_detail"),
]
