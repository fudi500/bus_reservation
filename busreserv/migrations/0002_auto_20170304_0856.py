# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='EndDate',
            field=models.DateField(),
        ),
    ]
