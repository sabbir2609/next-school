import random
from django.core.management.base import BaseCommand

from faker import Faker
import faker.providers

from school.models import Student
from school.models import Class


class Command(BaseCommand):
    help = "This command creates many users"

    def handle(self, *args, **options):
        fake = Faker()
        fake_bn = Faker("bn_BD")

        def phone():
            return f"01{random.randint(100000000, 999999999)}"

        def get_class():
            data = Class.objects.all()
            return random.choice(data)

        self.stdout.write(self.style.SUCCESS("Creating students..."))
        for _ in range(50):
            Student.objects.create(
                student_id=random.randint(100000, 999999),
                name_en=fake.name(),
                name_bn=fake_bn.name(),
                birth_certificate_no=fake.ssn(),
                gender=random.choice(["M", "F"]),
                religion=random.choice(["M", "H", "C", "B", "O"]),
                blood_group=random.choice(
                    ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
                ),
                date_of_birth=fake.date_of_birth(),
                phone=phone(),
                email=fake.email(),
                nationality=fake.country(),
                fathers_name_en=fake.name(),
                fathers_name_bn=fake_bn.name(),
                fathers_occupation=fake.job(),
                fathers_nid=fake.ssn(),
                fathers_phone=phone(),
                mothers_name_en=fake.name(),
                mothers_name_bn=fake_bn.name(),
                mothers_occupation=fake.job(),
                mothers_nid=fake.ssn(),
                mothers_phone=phone(),
                present_address=fake.address(),
                permanent_address=fake.address(),
                admission_class=get_class(),
                admission_date=fake.date(),
                comment=fake.text(),
                status=random.choice(["True", "False"]),
            )
        self.stdout.write(self.style.SUCCESS("Students created!"))
