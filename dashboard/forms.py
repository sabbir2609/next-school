from django import forms
from homepage.models import Notice
from taggit.forms import TagWidget
from dal import autocomplete


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
