# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('driverName', models.CharField(max_length=30)),
                ('driverPhone', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reDate',
            field=models.DateField(help_text='Date of reservation'),
        ),
    ]
