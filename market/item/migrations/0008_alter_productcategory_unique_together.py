# Generated by Django 4.2.7 on 2023-12-10 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_alter_product_price_productcategory'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productcategory',
            unique_together={('category', 'product')},
        ),
    ]