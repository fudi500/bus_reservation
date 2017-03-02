# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0008_auto_20170302_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reBusID',
            field=models.ForeignKey(to='busreserv.Bus', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reClientID',
            field=models.ForeignKey(to='busreserv.Client', blank=True, null=True),
        ),
    ]
