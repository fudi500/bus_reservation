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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('description', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=150)),
                ('plate_nr', models.CharField(max_length=10)),
                ('people_capacity', models.IntegerField()),
                ('price_per_km', models.DecimalField(decimal_places=2, max_digits=5)),
                ('available_for_cutomers', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('clientName', models.CharField(max_length=30)),
                ('clientEmail', models.EmailField(max_length=254)),
                ('clientPhone', models.CharField(max_length=15)),
                ('reDate', models.DateField()),
                ('km', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('details', models.CharField(max_length=200)),
                ('reBusID', models.ForeignKey(to='busreserv.Bus')),
            ],
        ),
    ]
