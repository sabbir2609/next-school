from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("school.urls", "school"), name="school"),
    path("", include("homepage.urls", "homepage"), name="homepage"),
    path("", include("user.urls", "user"), name="user"),
    path("", include("dashboard.urls", "dashboard"), name="dashboard"),
]

urlpatterns.extend(
    [
        path("ckeditor/", include("ckeditor_uploader.urls")),
    ]
)


# Admin Site Config
admin.site.site_header = "Turbo School Management System"
admin.site.site_title = "Turbo School Management System"
admin.site.index_title = "Welcome to Turbo School Management System"


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # Django Debug Toolbar

    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
