# Generated by Django 4.1.4 on 2022-12-14 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_account_options_alter_availability_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailabilityName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Доступность (список)',
                'verbose_name_plural': 'Доступность товаров (список)',
            },
        ),
        migrations.AlterField(
            model_name='availability',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.availabilityname'),
        ),
    ]
