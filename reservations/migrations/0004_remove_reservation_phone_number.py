# Generated by Django 3.2.18 on 2023-03-24 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_auto_20230317_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='phone_number',
        ),
    ]
