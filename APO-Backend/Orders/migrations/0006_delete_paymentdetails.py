# Generated by Django 4.1.6 on 2023-02-08 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0005_paymentdetails'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PaymentDetails',
        ),
    ]
