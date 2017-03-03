# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('busreserv', '0012_auto_20170303_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='km',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
