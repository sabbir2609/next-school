from django import forms
from django.forms import inlineformset_factory
from homepage.models import Notice
from dal import autocomplete
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Row, Column

from school.models import Section, SectionSubject, Guardian, Attendance


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ["title", "date", "description", "attachment", "tags"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control "}),
            "date": forms.DateInput(attrs={"class": "form-control ", "type": "date"}),
            "description": forms.Textarea(attrs={"class": "form-control "}),
            "attachment": forms.FileInput(
                attrs={
                    "class": "form-control ",
                    "type": "file",
                    "accept": ".doc,.docx,.pdf",
                }
            ),
            "tags": autocomplete.TaggitSelect2(
                url="dashboard:notice_tag_autocomplete",
                attrs={"class": "form-control "},
            ),
        }


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ["class_name", "name", "description", "teacher", "seat"]

        widgets = {
            "name": forms.Select(attrs={"class": "form-select"}),
            "description": forms.TextInput(attrs={"class": "form-control "}),
            "class_name": forms.Select(attrs={"class": "form-select"}),
            "teacher": forms.Select(attrs={"class": "form-select"}),
            "seat": forms.NumberInput(attrs={"class": "form-control "}),
        }


class SectionUpdateForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ["class_name", "name", "description", "teacher", "seat"]

        widgets = {
            "name": forms.TextInput(
                attrs={"readonly": "readonly", "disabled": "disabled"}
            ),
            "description": forms.Textarea(attrs={"class": "form-control "}),
            "class_name": forms.TextInput(
                attrs={"readonly": "readonly", "disabled": "disabled"}
            ),
            "teacher": forms.Select(attrs={"class": "form-select"}),
            "seat": forms.NumberInput(attrs={"class": "form-control "}),
        }


class SectionSubjectForm(forms.ModelForm):
    class Meta:
        model = SectionSubject
        fields = "__all__"

        widgets = {
            "subject": forms.Select(attrs={"class": "form-select"}),
            "teacher": forms.Select(attrs={"class": "form-select"}),
            "period": forms.TextInput(attrs={"class": "form-control "}),
            "time": forms.TimeInput(attrs={"type": "time", "class": "form-control "}),
        }


SectionSubjectFormset = inlineformset_factory(
    Section,
    SectionSubject,
    form=SectionSubjectForm,
    extra=1,
)


class GuardianForm(forms.ModelForm):
    class Meta:
        model = Guardian
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control "}),
            "phone": forms.TextInput(attrs={"class": "form-control "}),
            "address": forms.TextInput(attrs={"class": "form-control "}),
        }


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = "__all__"

        widgets = {
            "date": forms.DateInput(attrs={"class": "form-control ", "type": "date"}),
        }
