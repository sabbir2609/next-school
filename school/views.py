from dal import autocomplete

from .models import (
    StudentAssign,
)


# student autocomplete view for student assign
class StudentAutocompleteView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = StudentAssign.objects.all()

        if self.q:
            qs = qs.filter(student__name_en__istartswith=self.q)
        return qs
