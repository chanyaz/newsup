# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0013_topn_hindi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hindi_Business_Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Cluster_Id', models.IntegerField(db_index=True)),
                ('VideoId', models.CharField(max_length=100)),
                ('Title', models.CharField(max_length=100)),
                ('Summary', models.CharField(max_length=300)),
                ('Thumbnail', models.URLField(max_length=300, null=True, blank=True)),
                ('Published_Date', models.DateTimeField()),
                ('Duration', models.CharField(max_length=50)),
                ('Is_Rep', models.BooleanField(default=False)),
                ('Source', models.ForeignKey(to='newsApp.Video_Source')),
                ('Video', models.ForeignKey(to='newsApp.News_Video')),
            ],
        ),
        migrations.CreateModel(
            name='Hindi_Entertainment_Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Cluster_Id', models.IntegerField(db_index=True)),
                ('VideoId', models.CharField(max_length=100)),
                ('Title', models.CharField(max_length=100)),
                ('Summary', models.CharField(max_length=300)),
                ('Thumbnail', models.URLField(max_length=300, null=True, blank=True)),
                ('Published_Date', models.DateTimeField()),
                ('Duration', models.CharField(max_length=50)),
                ('Is_Rep', models.BooleanField(default=False)),
                ('Source', models.ForeignKey(to='newsApp.Video_Source')),
                ('Video', models.ForeignKey(to='newsApp.News_Video')),
            ],
        ),
        migrations.CreateModel(
            name='Hindi_Top_Stories_Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Cluster_Id', models.IntegerField(db_index=True)),
                ('VideoId', models.CharField(max_length=100)),
                ('Title', models.CharField(max_length=100)),
                ('Summary', models.CharField(max_length=300)),
                ('Thumbnail', models.URLField(max_length=300, null=True, blank=True)),
                ('Published_Date', models.DateTimeField()),
                ('Duration', models.CharField(max_length=50)),
                ('Is_Rep', models.BooleanField(default=False)),
                ('Source', models.ForeignKey(to='newsApp.Video_Source')),
                ('Video', models.ForeignKey(to='newsApp.News_Video')),
            ],
        ),
    ]
