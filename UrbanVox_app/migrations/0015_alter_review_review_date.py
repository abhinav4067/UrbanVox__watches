# Generated by Django 5.0.3 on 2024-04-08 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UrbanVox_app', '0014_review_delete_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_date',
            field=models.DateField(null=True),
        ),
    ]
