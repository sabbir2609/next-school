# Generated by Django 4.2 on 2023-04-24 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Class",
            fields=[
                (
                    "title",
                    models.CharField(
                        choices=[
                            ("6", "Six"),
                            ("7", "Seven"),
                            ("8", "Eight"),
                            ("9", "Nine"),
                            ("10", "Ten"),
                        ],
                        max_length=2,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("description", models.TextField()),
            ],
            options={
                "verbose_name_plural": "Classes",
            },
        ),
        migrations.CreateModel(
            name="Exam",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("date", models.DateField()),
            ],
            options={
                "verbose_name_plural": "Exams",
            },
        ),
        migrations.CreateModel(
            name="Section",
            fields=[
                (
                    "title",
                    models.CharField(
                        choices=[
                            ("A", "A"),
                            ("B", "B"),
                            ("C", "C"),
                            ("Sc", "Science"),
                            ("Co", "Commerce"),
                            ("Ar", "Arts"),
                        ],
                        max_length=2,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Section Description, e.g. 'Section A of Class 6, total 30 students'"
                    ),
                ),
                (
                    "class_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="school.class"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Sections",
                "unique_together": {("title", "class_name")},
            },
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name_bn", models.CharField(max_length=255)),
                ("name_en", models.CharField(max_length=255)),
                ("dob", models.DateField(auto_now_add=True)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("M", "Male"), ("F", "Female")],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "religion",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("M", "Muslim"),
                            ("H", "Hindu"),
                            ("C", "Christian"),
                            ("B", "Buddhist"),
                            ("O", "Others"),
                        ],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "blood_group",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("A+", "A+"),
                            ("A-", "A-"),
                            ("B+", "B+"),
                            ("B-", "B-"),
                            ("O+", "O+"),
                            ("O-", "O-"),
                            ("AB+", "AB+"),
                            ("AB-", "AB-"),
                        ],
                        max_length=3,
                        null=True,
                    ),
                ),
                ("student_id", models.CharField(blank=True, max_length=7)),
                ("birth_certificate_no", models.CharField(blank=True, max_length=17)),
                ("mobile_no", models.CharField(blank=True, max_length=11, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "fathers_name_bn",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "fathers_name_en",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("fathers_nid", models.CharField(blank=True, max_length=17, null=True)),
                (
                    "fathers_occupation",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "fathers_mobile_no",
                    models.CharField(blank=True, max_length=11, null=True),
                ),
                (
                    "mothers_name_bn",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "mothers_name_en",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("mothers_nid", models.CharField(blank=True, max_length=17, null=True)),
                (
                    "mothers_occupation",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "mothers_mobile_no",
                    models.CharField(blank=True, max_length=11, null=True),
                ),
                ("present_address", models.TextField(blank=True, null=True)),
                ("permanent_address", models.TextField(blank=True, null=True)),
                (
                    "nationality",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("class_roll", models.CharField(max_length=3)),
                ("admission_date", models.DateField(auto_now_add=True)),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="student_photo"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "comment",
                    models.TextField(
                        blank=True,
                        help_text="eg: any record about that student",
                        null=True,
                    ),
                ),
                (
                    "section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="school.section"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Students",
                "unique_together": {("section", "class_roll")},
            },
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="school.section"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Subjects",
            },
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name_bn", models.CharField(max_length=255)),
                ("name_en", models.CharField(max_length=255)),
                ("dob", models.DateField(auto_now_add=True)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("M", "Male"), ("F", "Female")],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "religion",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("M", "Muslim"),
                            ("H", "Hindu"),
                            ("C", "Christian"),
                            ("B", "Buddhist"),
                            ("O", "Others"),
                        ],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "blood_group",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("A+", "A+"),
                            ("A-", "A-"),
                            ("B+", "B+"),
                            ("B-", "B-"),
                            ("O+", "O+"),
                            ("O-", "O-"),
                            ("AB+", "AB+"),
                            ("AB-", "AB-"),
                        ],
                        max_length=3,
                        null=True,
                    ),
                ),
                ("teacher_id", models.CharField(blank=True, max_length=7)),
                ("nid", models.CharField(blank=True, max_length=17)),
                ("mobile_no", models.CharField(blank=True, max_length=11, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("present_address", models.TextField(blank=True, null=True)),
                ("permanent_address", models.TextField(blank=True, null=True)),
                ("joining_date", models.DateField(auto_now_add=True)),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="teacher_photo"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name_plural": "Teachers",
            },
        ),
        migrations.CreateModel(
            name="TeacherAssign",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "subject",
                    models.ManyToManyField(related_name="subject", to="school.subject"),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="teacher",
                        to="school.teacher",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Teacher Assign",
            },
        ),
        migrations.CreateModel(
            name="ExamResult",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("marks", models.PositiveSmallIntegerField()),
                (
                    "exam",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="school.exam"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="school.student"
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="school.subject"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Exam Results",
            },
        ),
        migrations.CreateModel(
            name="ExamAttendance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(auto_now_add=True)),
                ("status", models.BooleanField(default=False)),
                (
                    "exam",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="school.exam"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="school.student"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Exam Attendances",
            },
        ),
        migrations.CreateModel(
            name="ExamAssign",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.BooleanField(default=False)),
                (
                    "exam",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="exam",
                        to="school.exam",
                    ),
                ),
                (
                    "section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="school.section"
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="school.subject"
                    ),
                ),
                (
                    "teacher",
                    models.ManyToManyField(
                        related_name="exam_teacher", to="school.teacher"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Exam Assign",
            },
        ),
        migrations.CreateModel(
            name="Attendance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(auto_now_add=True)),
                ("status", models.BooleanField(default=False)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="school.student"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Attendances",
            },
        ),
        migrations.CreateModel(
            name="StudentAssign",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "section",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="section",
                        to="school.section",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="student",
                        to="school.student",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Student Assign",
                "unique_together": {("student", "section")},
            },
        ),
    ]
