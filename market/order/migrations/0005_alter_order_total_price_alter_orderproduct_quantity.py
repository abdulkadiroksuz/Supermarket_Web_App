# Generated by Django 4.2.7 on 2023-12-16 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
