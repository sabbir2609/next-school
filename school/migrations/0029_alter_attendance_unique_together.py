# Generated by Django 4.2.4 on 2023-09-07 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0028_remove_examassign_year_exam_year'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('student_assign', 'date')},
        ),
    ]
