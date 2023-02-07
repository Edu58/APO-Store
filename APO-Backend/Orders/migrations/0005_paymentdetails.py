# Generated by Django 4.1.6 on 2023-02-07 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0004_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(default=0, max_length=100)),
                ('provider', models.CharField(max_length=15)),
                ('transaction_ID', models.CharField(blank=True, db_index=True, max_length=100, unique=True)),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Not Paid', 'NOt Paid')], default='Not Paid', max_length=8)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.order')),
            ],
        ),
    ]