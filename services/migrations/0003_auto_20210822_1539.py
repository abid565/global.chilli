# Generated by Django 3.2.6 on 2021-08-22 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='contact_no',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='total_person',
            field=models.IntegerField(),
        ),
    ]