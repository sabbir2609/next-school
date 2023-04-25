from .models import Student, StudentAssign
from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

        exclude = [
            "admission_date",
            "status",
            "admission_class",
        ]

        widgets = {
            "dob": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }
