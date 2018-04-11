# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': ('canchange_entry', 'Can change the entries.'),
                'verbose_name_plural': 'entries',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('text', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserPerm',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('applicant', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('entry', models.ForeignKey(to='learning_logs.Entry')),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(to='learning_logs.Topic'),
        ),
        migrations.AddField(
            model_name='comment',
            name='entry',
            field=models.ForeignKey(to='learning_logs.Entry'),
        ),
        migrations.AddField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
