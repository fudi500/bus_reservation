# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0002_auto_20170304_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='EndDate',
            field=models.DateField(null=True, blank=True),
        ),
    ]
