# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0002_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('reDate', models.DateTimeField(blank=True, null=True)),
                ('km', models.IntegerField()),
                ('details', models.CharField(max_length=200)),
                ('reBusID', models.ForeignKey(to='busreserv.Bus')),
                ('reClientID', models.ForeignKey(to='busreserv.Client')),
            ],
        ),
    ]
