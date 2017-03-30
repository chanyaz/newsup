# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0008_auto_20160201_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_feed',
            name='Type',
            field=models.CharField(default=b'JSON', max_length=20),
        ),
        migrations.AlterField(
            model_name='news_feed',
            name='URL',
            field=models.URLField(max_length=1000),
        ),
    ]
