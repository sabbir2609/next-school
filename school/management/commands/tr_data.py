import random
from django.core.management.base import BaseCommand

from faker import Faker
import faker.providers

from school.models import Teacher


class Command(BaseCommand):
    help = "This command creates many users"

    def handle(self, *args, **options):
        fake = Faker()
        fake_bn = Faker("bn_BD")

        def phone():
            return f"01{random.randint(100000000, 999999999)}"

        self.stdout.write(self.style.SUCCESS("Creating teacher..."))
        for _ in range(15):
            Teacher.objects.create(
                teacher_id=random.randint(100000, 999999),
                name_en=fake.name(),
                name_bn=fake_bn.name(),
                date_of_birth=fake.date_of_birth(),
                gender=random.choice(["M", "F"]),
                religion=random.choice(["Islam", "Hindu", "Buddha", "Christian"]),
                blood_group=random.choice(
                    ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
                ),
                nid=fake.ssn(),
                phone=phone(),
                email=fake.email(),
                present_address=fake.address(),
                permanent_address=fake.address(),
                joining_date=fake.date(),
            )
        self.stdout.write(self.style.SUCCESS("Teachers created!"))
