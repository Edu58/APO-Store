# Generated by Django 4.1.6 on 2023-02-10 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalogue', '0009_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='photos/products/'),
        ),
    ]
