# Generated by Django 2.2.6 on 2019-11-25 01:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0018_auto_20191124_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='exp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 11, 26, 1, 56, 51, 505326)),
        ),
    ]