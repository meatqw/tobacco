# Generated by Django 4.1.4 on 2022-12-14 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_availabilityname_alter_availability_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rest',
        ),
    ]
