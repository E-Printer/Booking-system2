# Generated by Django 4.2.17 on 2024-12-22 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='service',
            new_name='session',
        ),
    ]