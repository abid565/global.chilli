# Generated by Django 3.2.6 on 2021-08-22 10:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('booking_date', models.DateField(default=datetime.date.today)),
                ('booking_time', models.CharField(max_length=20)),
                ('total_person', models.IntegerField(max_length=2)),
                ('contact_no', models.IntegerField(max_length=14)),
                ('message', models.TextField(max_length=100)),
                ('customer', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
