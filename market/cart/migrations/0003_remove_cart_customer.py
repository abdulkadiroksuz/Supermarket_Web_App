# Generated by Django 4.2.7 on 2023-12-14 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_cartproduct_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='customer',
        ),
    ]
