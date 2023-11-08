import random
from django.core.management.base import BaseCommand
from school.models import Section, Student, StudentAssign
from django.db import IntegrityError


class Command(BaseCommand):
    help = "This command assigns students to sections"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Assigning students..."))

        students = list(Student.objects.all())
        sections = list(Section.objects.all())

        for _ in range(50):
            student = random.choice(students)
            section = random.choice(sections)

            try:
                StudentAssign.objects.create(
                    student=student,
                    section=section,
                    class_roll=random.randint(1, 50),
                )
            except IntegrityError:
                self.stdout.write(
                    self.style.WARNING(
                        f"Skipped assignment for Student {student.student_id} in Section {section.id} (already assigned)."
                    )
                )

        self.stdout.write(self.style.SUCCESS("Students assigned!"))
