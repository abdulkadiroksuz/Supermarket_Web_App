# Generated by Django 4.2.7 on 2023-12-16 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_adress'),
        ('order', '0003_order_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.adress'),
        ),
    ]