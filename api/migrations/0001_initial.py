# Generated by Django 4.1.4 on 2022-12-09 04:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('info', models.TextField(blank=True, null=True, verbose_name='Информация')),
                ('img', models.ImageField(blank=True, upload_to='img/%Y/%m/%d', verbose_name='Изображение')),
                ('parent_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, verbose_name='Наименование')),
                ('img', models.ImageField(blank=True, upload_to='img/%Y/%m/%d', verbose_name='Изображение')),
                ('rest', models.IntegerField(blank=True, verbose_name='Остаток')),
                ('price', models.IntegerField(blank=True, verbose_name='Цена')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
                ('availability', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.availability')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.subcategory')),
                ('product_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.productstatus')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.JSONField(blank=True, null=True, verbose_name='Ордер лист')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Имя')),
                ('phone', models.CharField(max_length=300, verbose_name='Телефон')),
                ('email', models.CharField(max_length=300, verbose_name='Почта')),
                ('agents', models.CharField(max_length=300, verbose_name='Контрагенты')),
                ('address', models.CharField(max_length=300, verbose_name='Адреса')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
