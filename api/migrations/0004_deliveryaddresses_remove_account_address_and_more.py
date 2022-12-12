# Generated by Django 4.1.4 on 2022-12-12 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_userorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryAddresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300, verbose_name='Адрес')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='account',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userorder',
            name='status',
        ),
        migrations.AddField(
            model_name='userorder',
            name='number',
            field=models.CharField(default='', max_length=300, verbose_name='Номер заказа'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userorder',
            name='order_status',
            field=models.CharField(default='', max_length=300, verbose_name='Статус заказа'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userorder',
            name='pay_status',
            field=models.CharField(default='1', max_length=300, verbose_name='Статус оплаты'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userorder',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.deliveryaddresses'),
        ),
    ]
