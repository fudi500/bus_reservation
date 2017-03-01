# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0005_auto_20170227_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('firstName', models.CharField(max_length=15)),
                ('lasttName', models.CharField(max_length=15)),
                ('clientEmail', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('ReBusID', models.ForeignKey(to='busreserv.Bus')),
            ],
        ),
    ]
