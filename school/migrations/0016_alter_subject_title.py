# Generated by Django 4.2.4 on 2023-08-29 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0015_alter_examassign_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='title',
            field=models.CharField(help_text='Subject Name', max_length=255, unique=True),
        ),
    ]
