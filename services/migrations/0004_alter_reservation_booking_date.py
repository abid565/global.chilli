# Generated by Django 3.2.6 on 2021-08-22 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20210822_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='booking_date',
            field=models.CharField(max_length=20),
        ),
    ]
