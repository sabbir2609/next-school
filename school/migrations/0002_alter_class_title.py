# Generated by Django 4.2.4 on 2023-10-20 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='title',
            field=models.CharField(choices=[('Six', 'Six'), ('Seven', 'Seven'), ('Eight', 'Eight'), ('Nine', 'Nine'), ('Ten', 'Ten')], max_length=8, primary_key=True, serialize=False),
        ),
    ]
