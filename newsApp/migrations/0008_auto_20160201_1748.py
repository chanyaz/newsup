# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0007_auto_20160128_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hindi_Top_Stories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Cluster_Id', models.IntegerField(db_index=True)),
                ('URL', models.URLField(max_length=300)),
                ('Title', models.CharField(max_length=100)),
                ('Summary', models.CharField(max_length=300)),
                ('Thumbnail', models.URLField(max_length=300, null=True, blank=True)),
                ('Published_Date', models.DateTimeField()),
                ('Is_Rep', models.BooleanField(default=False)),
                ('Article', models.ForeignKey(to='newsApp.News_Article')),
                ('Source', models.ForeignKey(to='newsApp.News_Source')),
            ],
        ),
        migrations.RemoveField(
            model_name='news_feed1',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='news_feed1',
            name='Language',
        ),
        migrations.RemoveField(
            model_name='news_feed1',
            name='Source',
        ),
        migrations.DeleteModel(
            name='News_Feed1',
        ),
    ]
