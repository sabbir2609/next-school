# Generated by Django 4.2 on 2023-05-05 19:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0004_alter_class_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="section",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Section Description, e.g. 'Section A of Class 6, total 30 students'",
                null=True,
            ),
        ),
    ]
