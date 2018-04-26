# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0012_auto_20180413_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
