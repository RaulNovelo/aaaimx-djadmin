# Generated by Django 2.2.6 on 2019-11-22 19:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0010_auto_20191122_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='exp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 23, 19, 20, 36, 158849)),
        ),
    ]