# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0006_auto_20170302_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='clientEmail',
            field=models.CharField(max_length=15),
        ),
    ]
