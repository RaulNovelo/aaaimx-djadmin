# Generated by Django 3.0.5 on 2020-06-14 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productivity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='thumbnailFile',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
