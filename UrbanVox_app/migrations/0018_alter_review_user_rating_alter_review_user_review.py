# Generated by Django 5.0.3 on 2024-04-08 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UrbanVox_app', '0017_review_review_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user_rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='user_review',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
