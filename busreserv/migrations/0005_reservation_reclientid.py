# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0004_remove_reservation_reclientid'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='reClientID',
            field=models.ForeignKey(to='busreserv.Client', default=1),
            preserve_default=False,
        ),
    ]
