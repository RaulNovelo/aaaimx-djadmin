# Generated by Django 2.2.6 on 2019-10-23 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productivity', '0004_auto_20191023_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='collaborators',
            field=models.ManyToManyField(to='productivity.Member', verbose_name='collaborators'),
        ),
        migrations.AlterField(
            model_name='project',
            name='responsible',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
