# Generated by Django 4.2.4 on 2023-08-30 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0022_alter_class_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'ordering': ('slug',), 'verbose_name_plural': 'Classes'},
        ),
        migrations.AlterField(
            model_name='class',
            name='title',
            field=models.CharField(choices=[('Six', 'Six'), ('Seven', 'Seven'), ('Eignt', 'Eight'), ('Nine', 'Nine'), ('Ten', 'Ten')], max_length=8, primary_key=True, serialize=False),
        ),
    ]
