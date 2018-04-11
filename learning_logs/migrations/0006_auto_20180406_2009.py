# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_auto_20180406_2008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'permissions': ('canchange_entry', 'Can change entries'), 'verbose_name_plural': 'entries'},
        ),
    ]
