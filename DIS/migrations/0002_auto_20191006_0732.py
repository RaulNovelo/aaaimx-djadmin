# Generated by Django 2.2.6 on 2019-10-06 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DIS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='esterilizado',
            field=models.BooleanField(default=False),
        ),
    ]
