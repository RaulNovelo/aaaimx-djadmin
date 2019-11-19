# Generated by Django 2.2.6 on 2019-11-17 06:07

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productivity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('description', models.TextField(blank=True, default='')),
                ('to', models.CharField(max_length=100)),
                ('qr_url', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, default='', upload_to='certs')),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default='', max_length=200)),
                ('stock', models.IntegerField(blank=True, default=0)),
                ('available', models.IntegerField(blank=True, default=0)),
                ('observations', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, null=True)),
                ('date_start', models.DateTimeField(blank=True)),
                ('date_end', models.DateTimeField(blank=True)),
                ('description', models.TextField(blank=True, default='')),
                ('type', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('flyer', models.ImageField(blank=True, default=None, null=True, upload_to='flyers')),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='productivity.Division')),
            ],
        ),
    ]
