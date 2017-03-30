# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0004_topn_english_video_topn_marathi_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_feed',
            name='URL',
            field=models.URLField(max_length=500),
        ),
    ]
