# Generated by Django 5.0.3 on 2024-04-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UrbanVox_app', '0019_review_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_like',
            field=models.IntegerField(null=True),
        ),
    ]