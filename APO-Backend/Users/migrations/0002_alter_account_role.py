# Generated by Django 4.1.6 on 2023-02-10 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.CharField(choices=[('Customer', 'Customer'), ('Admin', 'Admin')], default='Customer', max_length=8),
        ),
    ]
