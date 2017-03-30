# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0002_auto_20151001_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='English_Business_Video',
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
            name='English_Environment_Video',
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
            name='English_Fashion_Video',
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
            name='English_Food_Video',
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
            name='English_Health_Video',
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
            name='English_Lifestyle_Video',
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
            name='English_Science_Video',
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
            name='English_Technology_Video',
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
            name='English_World_Video',
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
