from django.core.management.base import BaseCommand
from homepage.models import Notice
from faker import Faker
import random


class Command(BaseCommand):
    help = "Set fake notice data"

    def handle(self, *args, **options):
        fake = Faker()

        for _ in range(10):  # Generate 10 fake notices
            title = fake.sentence()
            description = fake.paragraph()
            attachment = "tools/notice1.pdf"  # Adjust the path to a sample PDF file
            date = fake.date_this_decade()

            Notice.objects.create(
                title=title, description=description, attachment=attachment, date=date
            )

        self.stdout.write(self.style.SUCCESS("Successfully set fake notice data."))
