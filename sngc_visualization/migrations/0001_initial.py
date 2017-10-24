# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 19:34
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppLogs',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, primary_key=True, serialize=False)),
                ('app_name', models.CharField(default=None, max_length=40)),
                ('logs', models.CharField(default=None, max_length=40)),
                ('timeline', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='InternetLogs',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid1, primary_key=True, serialize=False)),
                ('url', models.CharField(default=None, max_length=40)),
                ('logs', models.CharField(default=None, max_length=40)),
                ('added_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]