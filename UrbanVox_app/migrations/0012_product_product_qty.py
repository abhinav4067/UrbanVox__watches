# Generated by Django 5.0.3 on 2024-04-03 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UrbanVox_app', '0011_alter_user_reg_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_qty',
            field=models.IntegerField(default=1),
        ),
    ]
