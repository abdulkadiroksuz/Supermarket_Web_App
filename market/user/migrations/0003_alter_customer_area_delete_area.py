# Generated by Django 4.2.7 on 2023-12-02 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
        ('user', '0002_area_customer_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='storage.area'),
        ),
        migrations.DeleteModel(
            name='Area',
        ),
    ]
