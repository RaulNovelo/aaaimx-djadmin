# Generated by Django 2.2.6 on 2019-11-22 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='qr_url',
            new_name='QR',
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='date_created',
        ),
    ]