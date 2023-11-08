from django.core.management.base import BaseCommand
from school.models import Class, Section, Teacher
from faker import Faker
from django.core.exceptions import ValidationError
import random


class Command(BaseCommand):
    help = "Generate and save fake section data"

    def handle(self, *args, **options):
        fake = Faker()

        class_names = [
            Class.ClassChoices.CLASS_6,
            Class.ClassChoices.CLASS_7,
            Class.ClassChoices.CLASS_8,
            Class.ClassChoices.CLASS_9,
            Class.ClassChoices.CLASS_10,
        ]

        teachers = list(Teacher.objects.all())

        for class_name in class_names:
            if class_name in [
                Class.ClassChoices.CLASS_6,
                Class.ClassChoices.CLASS_7,
                Class.ClassChoices.CLASS_8,
            ]:
                section_choices = [
                    ("A", "Section A"),
                    ("B", "Section B"),
                    ("C", "Section C"),
                ]
            else:
                section_choices = [
                    ("Sc", "Science"),
                    ("Co", "Commerce"),
                    ("Ar", "Arts"),
                ]

            class_instance, created = Class.objects.get_or_create(title=class_name)

            for section_name, section_description in section_choices:
                try:
                    section_obj, created = Section.objects.get_or_create(
                        name=section_name,
                        class_name=class_instance,
                        defaults={
                            "description": section_description,
                            "teacher": random.choice(teachers) if teachers else None,
                            "seat": fake.random_int(min=20, max=40),
                        },
                    )
                    if created:
                        self.stdout.write(
                            f"Created {section_obj.name} section for Class {class_instance.title}"
                        )
                    else:
                        self.stdout.write(
                            f"{section_obj.name} section for Class {class_instance.title} already exists"
                        )
                except ValidationError as e:
                    self.stderr.write(f"Error: {e}")
