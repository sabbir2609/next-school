# Generated by Django 4.2.4 on 2023-10-20 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_remove_whatshappening_url_alter_stat_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='whatshappening',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
