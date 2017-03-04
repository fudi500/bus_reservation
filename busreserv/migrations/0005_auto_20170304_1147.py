# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0004_reservation_numofdays'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='numOfDays',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
