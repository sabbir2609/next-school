# Generated by Django 4.2.4 on 2023-11-14 09:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_alter_attendance_unique_together_attendance_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.date.today, editable=False),
        ),
    ]
