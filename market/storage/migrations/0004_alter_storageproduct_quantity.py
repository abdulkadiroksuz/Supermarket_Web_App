
# Generated by Django 4.2.7 on 2023-12-11 11:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0003_rename_companyid_storage_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storageproduct',
            name='quantity',
            field=models.IntegerField(default=100, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
