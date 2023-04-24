# Generated by Django 4.2 on 2023-04-23 05:59

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
                    "id",
                    models.PositiveSmallIntegerField(primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=100)),
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("date", models.DateField()),
            ],
            options={
                "verbose_name_plural": "Exams",
            },
        ),
        migrations.CreateModel(
            name="Parent",
            fields=[
                (
                    "id",
                    models.PositiveSmallIntegerField(primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Section",
            fields=[
                (
                    "id",
                    models.PositiveSmallIntegerField(primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "class_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="school.class"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Sections",
            },
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.PositiveSmallIntegerField(primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="school.parent"
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
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
                    models.PositiveSmallIntegerField(primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
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
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="school.subject"
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="school.teacher"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Teacher Assign",
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
                        on_delete=django.db.models.deletion.CASCADE, to="school.section"
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
                "verbose_name_plural": "Student Assign",
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
                (
                    "exam",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="school.exam"
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
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="school.teacher"
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
                ("date", models.DateField()),
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
    ]
