# Generated by Django 4.1.6 on 2023-02-07 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Catalogue', '0003_alter_discount_discount_percent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discount',
            old_name='desc',
            new_name='description',
        ),
    ]
