# Generated by Django 5.0.3 on 2024-03-24 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UrbanVox_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_offer',
            field=models.IntegerField(null=True),
        ),
    ]
