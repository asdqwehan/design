# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0010_auto_20180406_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='entrytitle',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
