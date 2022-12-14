# Generated by Django 4.1.4 on 2022-12-28 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_productlist_product_list'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productlist',
            options={'verbose_name': 'Список товаров', 'verbose_name_plural': 'Списки товаров'},
        ),
        migrations.RemoveField(
            model_name='productlist',
            name='info',
        ),
        migrations.AddField(
            model_name='productlist',
            name='carton',
            field=models.IntegerField(blank=True, null=True, verbose_name='Блок'),
        ),
        migrations.AddField(
            model_name='productlist',
            name='rrc',
            field=models.IntegerField(blank=True, null=True, verbose_name='РРЦ'),
        ),
    ]
