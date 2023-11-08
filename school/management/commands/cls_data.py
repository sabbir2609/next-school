from django.core.management.base import BaseCommand
from school.models import Class


class Command(BaseCommand):
    help = "Generate fake class data"

    def handle(self, *args, **options):
        from faker import Faker
        from django.utils.text import slugify
        from school.models import Class

        fake = Faker()
        classes = Class.CLASS_CHOICES

        for class_choice in classes:
            class_title, _ = class_choice

            class_obj, created = Class.objects.get_or_create(
                title=class_title,
                defaults={
                    "slug": slugify(class_title),
                    "class_teacher": None,  # Set a teacher if needed
                    "description": fake.sentence(),
                },
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Created {class_obj.title} class")
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS(f"{class_obj.title} class already exists")
                )
