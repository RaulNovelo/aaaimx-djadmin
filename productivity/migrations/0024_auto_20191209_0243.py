# Generated by Django 2.2.6 on 2019-12-09 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productivity', '0023_auto_20191209_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]