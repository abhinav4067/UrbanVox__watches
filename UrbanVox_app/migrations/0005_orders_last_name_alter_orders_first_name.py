# Generated by Django 5.0.3 on 2024-03-25 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UrbanVox_app', '0004_orders_city_orders_country_orders_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]