# Generated by Django 4.1.6 on 2023-02-10 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalogue', '0007_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.png', upload_to='photos/products/'),
        ),
    ]
