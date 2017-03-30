# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0005_auto_20160127_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_feed',
            name='URL',
            field=models.CharField(max_length=500),
        ),
    ]
