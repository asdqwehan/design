# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0007_auto_20180406_2009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'permissions': ('canchange', 'Can change'), 'verbose_name_plural': 'entries'},
        ),
    ]
