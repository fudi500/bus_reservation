# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0002_auto_20170303_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='currentDriver',
            field=models.ForeignKey(null=True, to='busreserv.Driver', blank=True),
        ),
    ]
