# Generated by Django 4.1.6 on 2023-02-10 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0006_delete_paymentdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='Not Provided', max_length=250),
            preserve_default=False,
        ),
    ]
