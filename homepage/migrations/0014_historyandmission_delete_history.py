# Generated by Django 4.2.4 on 2023-10-21 06:43

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0013_history_alter_brightstudent_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoryAndMission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('slug', models.SlugField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'History and Mission',
            },
        ),
        migrations.DeleteModel(
            name='History',
        ),
    ]