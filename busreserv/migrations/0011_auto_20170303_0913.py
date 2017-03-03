# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0010_auto_20170303_0848'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='lastName',
        ),
        migrations.AddField(
            model_name='reservation',
            name='clientName',
            field=models.CharField(max_length=30, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reBusID',
            field=models.ForeignKey(to='busreserv.Bus'),
        ),
    ]
