# Generated by Django 2.2.6 on 2020-03-16 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0010_certificate_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
