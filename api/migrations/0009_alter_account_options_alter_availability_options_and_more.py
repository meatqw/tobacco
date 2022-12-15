# Generated by Django 4.1.4 on 2022-12-14 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_userorder_payment_method_userorder_way_get'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterModelOptions(
            name='availability',
            options={'verbose_name': 'Доступность', 'verbose_name_plural': 'Доступность товаров'},
        ),
        migrations.AlterModelOptions(
            name='banners',
            options={'verbose_name': 'Баннер', 'verbose_name_plural': 'Баннеры'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Основные категории товаров'},
        ),
        migrations.AlterModelOptions(
            name='deliveryaddresses',
            options={'verbose_name': 'Адрес доставки', 'verbose_name_plural': 'Адреса доставки'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Промежуточные данные заказа'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Список товаров'},
        ),
        migrations.AlterModelOptions(
            name='productstatus',
            options={'verbose_name': 'Статус', 'verbose_name_plural': 'Статусы товаров'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'Подкатегория', 'verbose_name_plural': 'Подкатегории товаров'},
        ),
        migrations.AlterModelOptions(
            name='userorder',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AddField(
            model_name='availability',
            name='rest',
            field=models.IntegerField(blank=True, default=1, verbose_name='Остаток'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='product',
            name='availability',
        ),
        migrations.AddField(
            model_name='product',
            name='availability',
            field=models.ManyToManyField(to='api.availability'),
        ),
    ]
