# Generated by Django 4.2 on 2023-04-26 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="studentassign",
            options={},
        ),
        migrations.AlterField(
            model_name="studentassign",
            name="section",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="section_assignments",
                to="school.section",
            ),
        ),
        migrations.AlterField(
            model_name="studentassign",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="student_assignments",
                to="school.student",
            ),
        ),
        migrations.AlterField(
            model_name="subject",
            name="description",
            field=models.TextField(
                blank=True, help_text="Subject Description", null=True
            ),
        ),
        migrations.AlterField(
            model_name="subject",
            name="title",
            field=models.CharField(help_text="Subject Name", max_length=255),
        ),
    ]
