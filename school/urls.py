from django.urls import include, path

from .views import (
    StudentAutocompleteView,
)

app_name = "school"


# fmt: off
urlpatterns = [
    # Student Autocomplete URLs for assigned students
    path("student-autocomplete/", StudentAutocompleteView.as_view(), name="student-autocomplete"),

]
