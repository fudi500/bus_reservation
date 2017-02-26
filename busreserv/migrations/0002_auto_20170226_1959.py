# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='author',
        ),
        migrations.AlterField(
            model_name='bus',
            name='price_per_km',
            field=models.CharField(max_length=5),
        ),
    ]
