# Generated by Django 4.2.7 on 2023-11-25 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_customer_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='token',
            field=models.CharField(blank='', default='', max_length=250, null=''),
        ),
    ]
