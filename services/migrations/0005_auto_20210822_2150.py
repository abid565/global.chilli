# Generated by Django 3.2.6 on 2021-08-22 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0004_alter_reservation_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='message',
            field=models.TextField(max_length=50),
        ),
    ]
