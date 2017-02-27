# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0002_auto_20170226_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='price_per_km',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]
