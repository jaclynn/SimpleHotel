# Generated by Django 3.1.7 on 2021-03-26 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_booking_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
