# Generated by Django 4.2 on 2023-04-24 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0003_alter_student_unique_together_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="photo",
            new_name="image",
        ),
        migrations.AddField(
            model_name="student",
            name="admission_section",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="school.section",
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="status",
            field=models.BooleanField(default=True),
        ),
    ]
