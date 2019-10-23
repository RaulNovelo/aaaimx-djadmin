# Generated by Django 2.2.6 on 2019-10-21 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productivity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(blank=True, default='', max_length=100)),
                ('concept', models.TextField(blank=True, default='')),
                ('amount', models.FloatField(blank=True, default=0)),
                ('type', models.TextField(blank=True, default='')),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='productivity.Division')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.CharField(blank=True, default='', max_length=100)),
                ('concept', models.TextField(blank=True, default='')),
                ('amount', models.FloatField(blank=True, default=0)),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='productivity.Division')),
            ],
        ),
    ]
