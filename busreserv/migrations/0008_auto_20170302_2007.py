# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0007_auto_20170302_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reBusID',
            field=models.ForeignKey(null=True, to='busreserv.Bus'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reClientID',
            field=models.ForeignKey(null=True, to='busreserv.Client'),
        ),
    ]
