# Generated by Django 3.0.5 on 2020-04-26 08:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0052_auto_20200426_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='exp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 27, 8, 37, 44, 152687)),
        ),
    ]