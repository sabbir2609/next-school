from .models import Student, StudentAssign, Attendance
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


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = "__all__"

        widgets = {
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }
