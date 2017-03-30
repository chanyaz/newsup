# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0003_english_business_video_english_environment_video_english_fashion_video_english_food_video_english_he'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopN_English_Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('VideoId', models.CharField(max_length=100)),
                ('URL', models.URLField(max_length=300)),
                ('Title', models.CharField(max_length=100)),
                ('Summary', models.CharField(max_length=300)),
                ('Thumbnail', models.URLField(max_length=300, null=True, blank=True)),
                ('Published_Date', models.DateTimeField()),
                ('Source', models.ForeignKey(to='newsApp.Video_Source')),
                ('Video', models.ForeignKey(to='newsApp.News_Video')),
            ],
        ),
        migrations.CreateModel(
            name='TopN_Marathi_Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('VideoId', models.CharField(max_length=100)),
                ('URL', models.URLField(max_length=300)),
                ('Title', models.CharField(max_length=100)),
                ('Summary', models.CharField(max_length=300)),
                ('Thumbnail', models.URLField(max_length=300, null=True, blank=True)),
                ('Published_Date', models.DateTimeField()),
                ('Source', models.ForeignKey(to='newsApp.Video_Source')),
                ('Video', models.ForeignKey(to='newsApp.News_Video')),
            ],
        ),
    ]
