# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('description', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=150)),
                ('plate_nr', models.CharField(max_length=10)),
                ('people_capacity', models.IntegerField()),
                ('price_per_km', models.DecimalField(max_digits=5, decimal_places=2)),
                ('available_for_cutomers', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('driverName', models.CharField(max_length=30)),
                ('driverPhone', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('clientName', models.CharField(max_length=30)),
                ('clientEmail', models.EmailField(max_length=254)),
                ('clientPhone', models.CharField(max_length=15)),
                ('reDate', models.DateField(help_text='Date of reservation')),
                ('EndDate', models.DateField(default=models.DateField(help_text='Date of reservation'))),
                ('km', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('details', models.CharField(max_length=200)),
                ('reBusID', models.ForeignKey(to='busreserv.Bus')),
            ],
        ),
        migrations.AddField(
            model_name='bus',
            name='currentDriver',
            field=models.ForeignKey(to='busreserv.Driver', null=True, blank=True),
        ),
    ]
