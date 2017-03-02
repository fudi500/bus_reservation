# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0005_reservation_reclientid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='clientEmail',
            field=models.EmailField(max_length=254),
        ),
    ]
