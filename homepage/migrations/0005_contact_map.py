# Generated by Django 4.2.4 on 2023-10-18 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_rename_title_usefullink_site_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='map',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
