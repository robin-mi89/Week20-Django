# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-17 20:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeSnippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime(2017, 6, 17, 20, 34, 2, 218667, tzinfo=utc))),
                ('modified', models.DateTimeField(default=datetime.datetime(2017, 6, 17, 20, 34, 2, 218667, tzinfo=utc))),
                ('snippet', models.TextField()),
            ],
        ),
    ]