# Generated by Django 2.2.6 on 2019-11-17 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productivity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='lines',
            field=models.ManyToManyField(blank=True, to='productivity.Line', verbose_name='research lines'),
        ),
        migrations.AlterField(
            model_name='research',
            name='projects',
            field=models.ManyToManyField(blank=True, to='productivity.Project', verbose_name='related projects'),
        ),
    ]
