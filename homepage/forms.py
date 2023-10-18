from django import forms
from .models import Contact
from django.forms import inlineformset_factory
from .models import Contact, PhoneNumber, EmailAddress


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
