# Generated by Django 4.1.6 on 2023-02-11 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Catalogue', '0011_alter_product_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discount',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'ordering': ('-created_at',)},
        ),
    ]
