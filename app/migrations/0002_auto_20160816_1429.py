# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='X',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='Y',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='online',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
