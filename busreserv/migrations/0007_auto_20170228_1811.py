# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0006_client_reservation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='lasttName',
            new_name='clientPhone',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='ReBusID',
            new_name='reBusID',
        ),
        migrations.AddField(
            model_name='client',
            name='lastName',
            field=models.CharField(default=datetime.datetime(2017, 2, 28, 17, 11, 15, 316285, tzinfo=utc), max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='details',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='km',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='reClientID',
            field=models.ForeignKey(default=1, to='busreserv.Client'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='reDate',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
    ]
