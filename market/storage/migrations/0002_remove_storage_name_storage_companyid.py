# Generated by Django 4.2.7 on 2023-12-10 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storage',
            name='name',
        ),
        migrations.AddField(
            model_name='storage',
            name='companyId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.company'),
        ),
    ]
