# Generated by Django 4.0.3 on 2022-03-27 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customer_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='is_active',
        ),
    ]
