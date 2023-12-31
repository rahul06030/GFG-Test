# Generated by Django 4.2.7 on 2023-11-25 07:27

import datetime
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
            name='Order',
            fields=[
                ('order_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.CharField(default='pending', max_length=25)),
                ('billing_address', models.TextField(max_length=1000)),
                ('delivery_address', models.TextField(max_length=1000)),
                ('payment_details', models.JSONField(blank=True, null=True)),
                ('additional_data', models.JSONField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('updated_on', models.DateTimeField(default=datetime.datetime(2023, 11, 25, 7, 27, 51, 179708))),
                ('creation', models.DateTimeField(default=datetime.datetime(2023, 11, 25, 7, 27, 51, 179713))),
                ('customer_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('title', models.TextField(max_length=200)),
                ('product_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_quantity', models.IntegerField(default=0)),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('min_quantity', models.IntegerField(default=1)),
                ('max_quantity', models.IntegerField(default=0)),
                ('additional_data', models.JSONField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('updated_on', models.DateTimeField(default=datetime.datetime(2023, 11, 25, 7, 27, 51, 179451))),
                ('creation', models.DateTimeField(default=datetime.datetime(2023, 11, 25, 7, 27, 51, 179460))),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('order_details_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField(default=0)),
                ('is_deleted', models.BooleanField(default=False)),
                ('updated_on', models.DateTimeField(default=datetime.datetime(2023, 11, 25, 7, 27, 51, 179886))),
                ('creation', models.DateTimeField(default=datetime.datetime(2023, 11, 25, 7, 27, 51, 179891))),
                ('order_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='product.order')),
                ('product_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
