# Generated by Django 4.2.7 on 2023-11-24 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0016_alter_exam_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='abustract_name',
            field=models.CharField(blank=True, help_text='Section Abstract Name, e.g. Section `Meghna`', max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(choices=[('A', 'Section A'), ('B', 'Section B'), ('C', 'Section C'), ('D', 'Section D')], max_length=2, verbose_name='Section'),
        ),
    ]
