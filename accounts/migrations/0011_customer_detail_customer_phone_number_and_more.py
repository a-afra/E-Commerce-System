# Generated by Django 4.0.3 on 2022-03-28 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_order_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='detail',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.BigIntegerField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='street_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
