# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0007_auto_20170228_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
