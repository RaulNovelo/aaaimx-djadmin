# Generated by Django 3.0.5 on 2021-01-01 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0005_auto_20201231_0648'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='corum',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='hours',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
