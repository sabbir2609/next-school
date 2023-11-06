# Generated by Django 4.2.4 on 2023-11-06 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_guardian_studentguardian_student_guardians'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guardian',
            name='relation',
        ),
        migrations.AddField(
            model_name='studentguardian',
            name='relation',
            field=models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Guardian', 'Guardian')], default='Guardian', max_length=8),
        ),
    ]
