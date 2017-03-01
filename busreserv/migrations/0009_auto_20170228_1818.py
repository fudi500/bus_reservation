# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0008_auto_20170228_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='reBusID',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='reClientID',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
    ]
