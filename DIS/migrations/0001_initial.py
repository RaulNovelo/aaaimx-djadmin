# Generated by Django 2.2.6 on 2019-10-06 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default='', max_length=100)),
                ('sexo', models.CharField(blank=True, default='', max_length=100)),
                ('mes_ingreso', models.DateField(blank=True, default=None)),
                ('esterilizado', models.BooleanField(blank=True, default=False)),
                ('edad', models.CharField(blank=True, default='', max_length=100)),
                ('peso', models.CharField(blank=True, default='', max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('vacunas', models.TextField(blank=True)),
                ('foto', models.ImageField(blank=True, default=None, null=True, upload_to='pets')),
            ],
        ),
    ]
