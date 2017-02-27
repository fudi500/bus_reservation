# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0003_auto_20170227_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='price_per_km',
            field=models.CharField(max_length=5),
        ),
    ]
