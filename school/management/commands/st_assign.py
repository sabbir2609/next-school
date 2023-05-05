import random

from django.core.management.base import BaseCommand

from school.models import Section, Student, StudentAssign


class Command(BaseCommand):
    help = "This command assigns students to sections"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Assigning students..."))
        
        def get_student():
            students = Student.objects.all()
            return students

        for _ in range(50):
            StudentAssign.objects.create(
                student=random.choice(get_student()),
                section=random.choice(Section.objects.all()),
                class_roll=random.randint(1, 50),
            )
        
        self.stdout.write(self.style.SUCCESS("Students assigned!"))