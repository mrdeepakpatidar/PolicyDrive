# Generated by Django 3.1.2 on 2021-01-05 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_lic_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lic',
            name='user',
        ),
    ]