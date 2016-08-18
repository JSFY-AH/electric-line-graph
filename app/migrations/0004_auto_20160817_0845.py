# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160817_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='root_x',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='line',
            name='root_y',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
