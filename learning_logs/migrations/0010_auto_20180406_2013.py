# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0009_auto_20180406_2013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'permissions': (('canchange_entry', 'Can change the entries'),), 'verbose_name_plural': 'entries'},
        ),
    ]
