from django import forms
from django.forms import inlineformset_factory
from homepage.models import Notice
from dal import autocomplete

from school.models import Section, SectionSubject


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
        fields = ["name", "description", "class_name", "teacher", "seat"]

        widgets = {
            "name": forms.Select(attrs={"class": "form-select"}),
            "description": forms.Textarea(attrs={"class": "form-control "}),
            "class_name": forms.Select(attrs={"class": "form-select"}),
            "teacher": forms.Select(attrs={"class": "form-select"}),
            "seat": forms.NumberInput(attrs={"class": "form-control "}),
        }


class SectionSubjectForm(forms.ModelForm):
    class Meta:
        model = SectionSubject
        fields = ["subject", "teachers", "period", "time"]

        widgets = {
            "subject": forms.Select(attrs={"class": "form-select"}),
            "teachers": forms.Select(attrs={"class": "form-select"}),
            "period": forms.TextInput(attrs={"class": "form-control "}),
            "time": forms.TextInput(attrs={"class": "form-control "}),
        }


SectionSubjectInlineFormset = inlineformset_factory(
    Section,
    SectionSubject,
    form=SectionSubjectForm,
    extra=1,
    can_delete=True,
    can_delete_extra=True,
)
