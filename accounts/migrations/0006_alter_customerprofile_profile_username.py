# Generated by Django 3.2.6 on 2021-08-29 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210825_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='profile_username',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
