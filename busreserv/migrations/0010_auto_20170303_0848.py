# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0009_auto_20170302_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='clientEmail',
        ),
        migrations.RemoveField(
            model_name='client',
            name='clientPhone',
        ),
        migrations.RemoveField(
            model_name='client',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='client',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='reClientID',
        ),
        migrations.AddField(
            model_name='reservation',
            name='clientEmail',
            field=models.EmailField(max_length=254, default=datetime.datetime(2017, 3, 3, 7, 47, 46, 450196, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='clientPhone',
            field=models.CharField(max_length=15, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='firstName',
            field=models.CharField(max_length=15, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='lastName',
            field=models.CharField(max_length=15, default=0),
            preserve_default=False,
        ),
    ]
