# Generated by Django 4.2.4 on 2023-08-28 18:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_alter_examassign_unique_together_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_type', models.CharField(choices=[('Half Yearly', 'Half Yearly'), ('Year Final', 'Year Final'), ('Pretest', 'Pretest'), ('Test', 'Test')], max_length=20)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='ExamAssign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_paper', models.FileField(blank=True, null=True, upload_to='question_paper')),
                ('full_mark', models.PositiveIntegerField(default=0)),
                ('pass_mark', models.PositiveIntegerField(default=0)),
                ('exam_time', models.TimeField(blank=True, null=True)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.exam')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.section')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.sectionsubject')),
            ],
            options={
                'unique_together': {('exam', 'section', 'subject')},
            },
        ),
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mcq_mark', models.PositiveIntegerField(default=0)),
                ('written_mark', models.PositiveIntegerField(default=0)),
                ('practical_mark', models.PositiveIntegerField(default=0)),
                ('exam_assign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.examassign')),
                ('student_assign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.studentassign')),
            ],
            options={
                'unique_together': {('exam_assign', 'student_assign')},
            },
        ),
    ]
