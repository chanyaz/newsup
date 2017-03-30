# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='english_entertainment_video',
            name='Duration',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='english_sports_video',
            name='Duration',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='english_top_stories_video',
            name='Duration',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='marathi_entertainment_video',
            name='Duration',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='marathi_sports_video',
            name='Duration',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='marathi_top_stories_video',
            name='Duration',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='news_video',
            name='Duration',
            field=models.CharField(max_length=50),
        ),
    ]
