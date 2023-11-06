# Generated by Django 4.2.4 on 2023-11-06 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_remove_student_guardians_guardian_relation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guardian',
            old_name='first_name',
            new_name='name_bn',
        ),
        migrations.RenameField(
            model_name='guardian',
            old_name='last_name',
            new_name='name_en',
        ),
        migrations.RenameField(
            model_name='guardian',
            old_name='phone_number',
            new_name='phone',
        ),
        migrations.AddField(
            model_name='guardian',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='guardian'),
        ),
        migrations.AddField(
            model_name='guardian',
            name='nid',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
