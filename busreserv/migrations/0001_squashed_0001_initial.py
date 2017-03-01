# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [('busreserv', '0001_initial')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('description', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=150)),
                ('plate_nr', models.CharField(max_length=10)),
                ('people_capacity', models.IntegerField()),
                ('price_per_km', models.IntegerField()),
                ('available_for_cutomers', models.BooleanField(default=True)),
            ],
        ),
    ]
