# Generated by Django 4.2.7 on 2023-11-25 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(default='pending', max_length=25),
        ),
        migrations.AlterField(
            model_name='order',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 25, 8, 33, 42, 125883)),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 25, 8, 33, 42, 125877)),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 25, 8, 33, 42, 126063)),
        ),
        migrations.AlterField(
            model_name='orderdetails',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 25, 8, 33, 42, 126058)),
        ),
        migrations.AlterField(
            model_name='product',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 25, 8, 33, 42, 125631)),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 25, 8, 33, 42, 125622)),
        ),
    ]
