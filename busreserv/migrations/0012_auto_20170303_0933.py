# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0011_auto_20170303_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reDate',
            field=models.DateField(),
        ),
    ]
