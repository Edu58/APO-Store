# Generated by Django 4.1.6 on 2023-02-10 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalogue', '0008_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=250),
        ),
    ]
