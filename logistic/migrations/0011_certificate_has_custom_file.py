# Generated by Django 3.0.5 on 2021-01-04 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0010_auto_20210102_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='has_custom_file',
            field=models.BooleanField(default=False),
        ),
    ]