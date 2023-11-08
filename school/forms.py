from django import forms

from .models import Teacher, Attendance, Student, StudentAssign, StudentResult

from dal import autocomplete


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

        exclude = [
            "admission_date",
            "status",
            "admission_class",
            "guardian",
        ]

        widgets = {
            "date_of_birth": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = "__all__"

        widgets = {
            "date_of_birth": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "joining_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
        }


# student assign form
class StudentAssignForm(forms.ModelForm):
    class Meta:
        model = StudentAssign
        fields = "__all__"
