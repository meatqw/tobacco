# Generated by Django 4.1.4 on 2022-12-06 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, upload_to='img/%Y/%m/%d', verbose_name='Изображение'),
        ),
    ]
