# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-04 12:02

"""
    (c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2017
"""

from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('sciper',
                 models.CharField(blank=True, max_length=100, null=True)),
                ('where',
                 models.CharField(blank=True, max_length=100, null=True)),
                ('units',
                 models.CharField(blank=True, max_length=300, null=True)),
                ('group',
                 models.CharField(blank=True, max_length=150, null=True)),
                ('classe',
                 models.CharField(blank=True, max_length=100, null=True)),
                ('statut',
                 models.CharField(blank=True, max_length=100, null=True)),
                ('memberof',
                 models.CharField(blank=True, max_length=300, null=True)),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
