from django import forms
from .models import Contact
from django.forms import inlineformset_factory
from .models import Contact, PhoneNumber, EmailAddress, Notice
from taggit.forms import TagWidget


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "address",
            "map",
        ]


PhoneNumberFormSet = inlineformset_factory(
    Contact, PhoneNumber, fields=("number",), extra=1, can_delete=True
)
EmailAddressFormSet = inlineformset_factory(
    Contact, EmailAddress, fields=("email",), extra=1, can_delete=True
)


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = "__all__"

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control "}),
            "slug": forms.TextInput(
                attrs={
                    "class": "form-control ",
                    "id": "disabled",
                    "readonly": "readonly",
                    "disabled": "disabled",
                }
            ),
            "date": forms.DateInput(attrs={"class": "form-control ", "type": "date"}),
            "description": forms.Textarea(attrs={"class": "form-control "}),
            "attachment": forms.FileInput(
                attrs={
                    "class": "form-control ",
                    "type": "file",
                    "accept": ".doc,.docx,.pdf",
                }
            ),
            "tags": TagWidget(
                attrs={"class": "", "data-role": "tagsinput"}
            ),  # TODO: make it nice
        }
