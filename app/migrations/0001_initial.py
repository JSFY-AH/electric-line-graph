# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.CharField(max_length=200)),
                ('father_id', models.IntegerField(default=-1)),
                ('node_type', models.IntegerField(default=0)),
            ],
        ),
    ]
