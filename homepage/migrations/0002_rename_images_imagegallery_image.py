# Generated by Django 4.2.4 on 2023-10-20 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagegallery',
            old_name='images',
            new_name='image',
        ),
    ]
