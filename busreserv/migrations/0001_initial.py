# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=150)),
                ('plate_nr', models.CharField(max_length=10)),
                ('people_capacity', models.IntegerField()),
                ('price_per_km', models.DecimalField(decimal_places=2, max_digits=5)),
                ('available_for_cutomers', models.BooleanField(default=True)),
            ],
        ),
    ]
