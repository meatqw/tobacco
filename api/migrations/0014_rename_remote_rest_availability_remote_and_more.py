# Generated by Django 4.1.4 on 2022-12-15 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_remove_availability_name_remove_availability_rest_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='availability',
            old_name='remote_rest',
            new_name='remote',
        ),
        migrations.RenameField(
            model_name='availability',
            old_name='in_stock_rest',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='availability',
            old_name='on_way_rest',
            new_name='way',
        ),
    ]
