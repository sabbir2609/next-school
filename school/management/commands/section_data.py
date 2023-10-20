from django.core.management.base import BaseCommand
from school.models import (
    Section,
    Class,
    Teacher,
    Subject,
    SectionSubject,
)  # Replace 'yourapp' with your app name


class Command(BaseCommand):
    help = "Generate fake section data"

    def handle(self, *args, **options):
        from faker import Faker

        fake = Faker()
        classes = Class.objects.all()

        for class_obj in classes:
            for section_choice in Section.SECTION_CHOICES:
                section_name, _ = section_choice

                section_obj, created = Section.objects.get_or_create(
                    name=section_name,
                    class_name=class_obj,
                    defaults={
                        "description": fake.sentence(),
                        "section_teacher": None,  # Set a teacher if needed
                        "seat": fake.random_int(min=20, max=40),
                    },
                )

                if created:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"Created {section_obj.name} section for {class_obj.title}"
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"{section_obj.name} section for {class_obj.title} already exists"
                        )
                    )

        self.stdout.write(self.style.SUCCESS("Fake section data generation complete"))
