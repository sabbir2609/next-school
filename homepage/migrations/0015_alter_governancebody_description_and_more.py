# Generated by Django 4.2.4 on 2023-10-21 07:11

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0014_historyandmission_delete_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='governancebody',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='governancebody',
            name='speech_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]