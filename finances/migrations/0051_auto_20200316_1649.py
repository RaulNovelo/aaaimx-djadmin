# Generated by Django 2.2.6 on 2020-03-16 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0050_auto_20200316_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='exp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 17, 16, 49, 17, 363657)),
        ),
    ]