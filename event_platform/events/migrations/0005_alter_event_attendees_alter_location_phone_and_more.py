# Generated by Django 4.2.4 on 2023-09-05 19:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0004_alter_event_host'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(blank=True, related_name='events_attending', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='location',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Contact Phone'),
        ),
        migrations.AlterField(
            model_name='location',
            name='zip_code',
            field=models.CharField(blank=True, max_length=10, verbose_name='Zip Code'),
        ),
    ]
