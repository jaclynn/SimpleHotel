# Generated by Django 3.1.7 on 2021-03-26 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_booking_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='occupied',
            field=models.BooleanField(default=False),
        ),
    ]
