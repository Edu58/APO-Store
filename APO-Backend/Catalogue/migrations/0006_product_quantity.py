# Generated by Django 4.1.6 on 2023-02-10 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalogue', '0005_rename_desc_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]