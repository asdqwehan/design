# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0011_entry_entrytitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
