# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0003_reservation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='reClientID',
        ),
    ]
